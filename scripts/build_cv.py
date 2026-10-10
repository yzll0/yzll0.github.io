#!/usr/bin/env python3
"""Build bilingual A4 PDFs from the CV webpages' Markdown, without LaTeX."""
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
LANGUAGES = {
    'en': ('_pages/cv.md', 'Weixuan_Yuan_CV', 'en', 'Weixuan Yuan — Curriculum Vitae'),
    'zh': ('_pages/zh/cv.md', 'Weixuan_Yuan_CV_zh', 'zh-CN', '袁伟轩 — 简历'),
}


def prepare_html(language):
    source, basename, html_lang, title = LANGUAGES[language]
    raw = (ROOT / source).read_text(encoding='utf-8')
    parts = re.split(r'^---\s*$', raw, maxsplit=2, flags=re.MULTILINE)
    if len(parts) != 3 or parts[0].strip():
        raise SystemExit(f'Expected Jekyll YAML front matter in {source}')
    body = parts[2].strip()
    if '{{' in body or '{%' in body:
        raise SystemExit(f'Keep {source} portable Markdown/HTML, without Liquid tags.')
    css = (ROOT / 'scripts/cv.css').read_text(encoding='utf-8')
    if language == 'zh':
        for weight, value in [('Regular', 400), ('Bold', 700)]:
            font = ROOT / f'scripts/fonts/NotoSerifSC-{weight}.woff2'
            if not font.exists():
                raise SystemExit(f'Missing bundled font: {font}')
            css += (f'\n@font-face {{font-family: "CV Noto Serif"; font-weight: {value}; '
                    f'src: url("{font.as_uri()}") format("woff2");}}')
    html_body = markdown.markdown(body, extensions=['extra'])
    html = (f'<!doctype html><html lang="{html_lang}"><head><meta charset="utf-8">'
            f'<title>{title}</title><style>{css}</style></head><body>{html_body}</body></html>')
    preview = ROOT / 'tmp/pdfs' / language
    preview.mkdir(parents=True, exist_ok=True)
    html_path = preview / f'{basename}.html'
    html_path.write_text(html, encoding='utf-8')
    return html_path, preview / f'{basename}.pdf'


def validate_pdf(candidate, language):
    reader = PdfReader(candidate)
    if not 1 <= len(reader.pages) <= 2:
        raise SystemExit(f'{language}: expected 1–2 pages, got {len(reader.pages)}; adjust scripts/cv.css.')
    for i, page in enumerate(reader.pages, 1):
        if len((page.extract_text() or '').strip()) < 100:
            raise SystemExit(f'{language}: page {i} has unexpectedly little extractable text.')
        for reference in page['/Resources']['/Font'].get_object().values():
            font = reference.get_object()
            if '/ToUnicode' not in font:
                raise SystemExit(f'{language}: a PDF font lacks a Unicode text map.')
            if font.get('/Subtype') == '/Type3':
                # Chromium may embed CFF glyph outlines as Type 3 drawing streams.
                glyphs = font['/CharProcs'].get_object()
                if not glyphs or not all(g.get_object().get_data() for g in glyphs.values()):
                    raise SystemExit(f'{language}: missing embedded glyph outlines.')
            else:
                for child in font.get('/DescendantFonts', [font]):
                    descriptor = child.get_object()['/FontDescriptor'].get_object()
                    if not any(key in descriptor for key in ['/FontFile', '/FontFile2', '/FontFile3']):
                        raise SystemExit(f'{language}: a PDF font is not embedded.')

    if language == 'zh':
        text = ''.join(page.extract_text() or '' for page in reader.pages)
        for phrase in ['袁伟轩', '少年班', '研究助理', '数学规格']:
            if phrase not in text:
                raise SystemExit(f'Chinese text extraction failed: {phrase}')
    return len(reader.pages)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lang', choices=['all', *LANGUAGES], default='all')
    parser.add_argument('--preview', action='store_true', help='Render every PDF page to PNG with pdftoppm')
    args = parser.parse_args()
    if args.preview and not shutil.which('pdftoppm'):
        raise SystemExit('Install Poppler (pdftoppm) to render PNG previews.')
    languages = list(LANGUAGES) if args.lang == 'all' else [args.lang]
    candidates = []
    with sync_playwright() as pw:
        options = {}
        if os.environ.get('CV_CHROME_PATH'):
            options['executable_path'] = os.environ['CV_CHROME_PATH']
        elif Path('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome').exists():
            options['channel'] = 'chrome'
        browser = pw.chromium.launch(**options)
        for language in languages:
            html_path, candidate = prepare_html(language)
            page = browser.new_page()
            # Only local Markdown, CSS, and bundled fonts; no network assets.
            page.route('http://**/*', lambda route: route.abort())
            page.route('https://**/*', lambda route: route.abort())
            page.goto(html_path.as_uri())
            page.evaluate('document.fonts.ready')
            if language == 'zh':
                for weight in [400, 700]:
                    loaded = page.evaluate('async weight => (await document.fonts.load(`${weight} 11px "CV Noto Serif"`, "中文")).length', weight)
                    if not loaded:
                        raise SystemExit('Bundled Chinese font failed to load.')
            page.pdf(path=str(candidate), format='A4', prefer_css_page_size=True,
                     print_background=True, display_header_footer=True,
                     header_template='<span></span>',
                     footer_template='<div style="width:100%;font-family:serif;font-size:9px;'
                     'text-align:center;color:#666">Weixuan Yuan · '
                     '<span class="pageNumber"></span> / <span class="totalPages"></span></div>')
            page.close()
            candidates.append((candidate, validate_pdf(candidate, language)))
        browser.close()
    # Do not replace either published artifact until all requested PDFs validate.
    for candidate, pages in candidates:
        output = ROOT / 'files' / candidate.name
        output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(candidate, output)
        print(f'Generated {output} ({pages} pages)')
        if args.preview:
            for stale in candidate.parent.glob('cv-page-*.png'):
                stale.unlink()
            subprocess.run(['pdftoppm', '-scale-to', '1600', '-png', str(output),
                            str(candidate.parent / 'cv-page')], check=True)
            print(f'Page previews: {candidate.parent}/cv-page-*.png')


if __name__ == '__main__':
    main()
