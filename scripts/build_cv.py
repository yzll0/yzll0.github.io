#!/usr/bin/env python3
"""Build an A4 PDF from the CV webpage's Markdown; no LaTeX or Jekyll needed."""
import argparse
import os
from pathlib import Path
import re
import shutil
import subprocess

import markdown
from playwright.sync_api import sync_playwright
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--preview', action='store_true', help='Render every PDF page to PNG with pdftoppm')
    args = parser.parse_args()
    source = ROOT / '_pages/cv.md'
    raw = source.read_text(encoding='utf-8')
    parts = re.split(r'^---\s*$', raw, maxsplit=2, flags=re.MULTILINE)
    if len(parts) != 3 or parts[0].strip():
        raise SystemExit('Expected Jekyll YAML front matter in _pages/cv.md')
    body = parts[2].strip()
    if '{{' in body or '{%' in body:
        raise SystemExit('Keep the CV body portable Markdown/HTML, without Liquid tags.')
    html_body = markdown.markdown(body, extensions=['extra'])
    css = (ROOT / 'scripts/cv.css').read_text(encoding='utf-8')
    html = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<title>Weixuan Yuan — Curriculum Vitae</title>'
            f'<style>{css}</style></head><body>{html_body}</body></html>')
    preview = ROOT / 'tmp/pdfs'
    preview.mkdir(parents=True, exist_ok=True)
    html_path = preview / 'Weixuan_Yuan_CV.html'
    html_path.write_text(html, encoding='utf-8')
    output = ROOT / 'files/Weixuan_Yuan_CV.pdf'
    output.parent.mkdir(parents=True, exist_ok=True)
    candidate = preview / 'Weixuan_Yuan_CV.pdf'
    with sync_playwright() as pw:
        options = {}
        if os.environ.get('CV_CHROME_PATH'):
            options['executable_path'] = os.environ['CV_CHROME_PATH']
        elif Path('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome').exists():
            options['channel'] = 'chrome'
        browser = pw.chromium.launch(**options)
        page = browser.new_page()
        # Rendering is offline: the CV contains hyperlinks, no fetched assets.
        page.route('http://**/*', lambda route: route.abort())
        page.route('https://**/*', lambda route: route.abort())
        page.goto(html_path.as_uri())
        page.evaluate('document.fonts.ready')
        page.pdf(path=str(candidate), format='A4', prefer_css_page_size=True,
                 print_background=True, display_header_footer=True,
                 header_template='<span></span>',
                 footer_template='<div style="width:100%;font-family:serif;font-size:9px;'
                 'text-align:center;color:#666">Weixuan Yuan · '
                 '<span class="pageNumber"></span> / <span class="totalPages"></span></div>')
        browser.close()
    reader = PdfReader(candidate)
    if not 1 <= len(reader.pages) <= 2:
        raise SystemExit(f'Expected 1–2 pages, got {len(reader.pages)}; adjust scripts/cv.css.')
    for i, pdf_page in enumerate(reader.pages, 1):
        if len((pdf_page.extract_text() or '').strip()) < 100:
            raise SystemExit(f'Page {i} has unexpectedly little extractable text.')
    shutil.copyfile(candidate, output)
    print(f'Generated {output} ({len(reader.pages)} pages)')
    if args.preview:
        if not shutil.which('pdftoppm'):
            raise SystemExit('PDF built. Install Poppler (pdftoppm) to render PNG previews.')
        for stale in preview.glob('cv-page-*.png'):
            stale.unlink()
        subprocess.run(['pdftoppm', '-scale-to', '1600', '-png', str(output),
                        str(preview / 'cv-page')], check=True)
        print(f'Page previews: {preview}/cv-page-*.png')


if __name__ == '__main__':
    main()
