#!/usr/bin/env python3
"""Check a Jekyll build for broken local links and accidentally published inputs."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / '_site'


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
        self.elements = []

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))
        for key, value in attrs:
            if key in ('href', 'src') and value:
                self.urls.append(value)



PAGE_PAIRS = [('/', '/zh/'), ('/publications/', '/zh/publications/'), ('/cv/', '/zh/cv/')]
PDFS = ['/files/Weixuan_Yuan_CV.pdf', '/files/Weixuan_Yuan_CV_zh.pdf']


def check_bilingual(errors):
    for pdf in PDFS:
        artifact = SITE / pdf.lstrip('/')
        source = ROOT / pdf.lstrip('/')
        if not artifact.exists() or not artifact.read_bytes().startswith(b'%PDF-'):
            errors.append(f'Missing or invalid PDF: {pdf}')
        elif not source.exists() or artifact.read_bytes() != source.read_bytes():
            errors.append(f'Stale published PDF: {pdf}')
    for pair in PAGE_PAIRS:
        expected = dict(zip(['en', 'zh-CN'], pair))
        for language, url in expected.items():
            page = SITE / url.lstrip('/') / 'index.html'
            if not page.exists():
                errors.append(f'Missing bilingual page: {url}')
                continue
            parser = Links()
            parser.feed(page.read_text(encoding='utf-8'))
            html = [attrs for tag, attrs in parser.elements if tag == 'html']
            if len(html) != 1 or html[0].get('lang') != language:
                errors.append(f'Incorrect HTML language: {url}')
            alternates = {a.get('hreflang'): urlsplit(a.get('href', '')).path
                          for tag, a in parser.elements if tag == 'link' and a.get('rel') == 'alternate' and a.get('hreflang')}
            if alternates != {**expected, 'x-default': pair[0]}:
                errors.append(f'Incorrect alternate language links: {url}')
            switches = {a.get('hreflang'): a for tag, a in parser.elements
                        if tag == 'a' and a.get('hreflang') in expected}
            for lang, target in expected.items():
                switch = switches.get(lang, {})
                if urlsplit(switch.get('href', '')).path != target:
                    errors.append(f'Incorrect {lang} language switch: {url}')
                if (switch.get('aria-current') == 'page') != (lang == language):
                    errors.append(f'Incorrect active language: {url}')
            if pair != PAGE_PAIRS[1]:
                downloads = [urlsplit(a.get('href', '')).path for tag, a in parser.elements
                             if tag == 'a' and 'download' in a]
                if any(pdf not in downloads for pdf in PDFS):
                    errors.append(f'Missing dual CV downloads: {url}')


def main():
    if not (SITE / 'index.html').exists():
        raise SystemExit('Run bundle exec jekyll build first.')
    errors = []
    count = 0
    forbidden = ['GitHub University', 'Paper Title Number', 'University 1, Department',
                 'Talk 1 on Relevant Topic', 'Lorem ipsum']
    for page in SITE.rglob('*.html'):
        text = page.read_text(encoding='utf-8')
        for phrase in forbidden:
            if phrase in text:
                errors.append(f'Template content: {page.relative_to(SITE)}: {phrase}')
        parser = Links()
        parser.feed(text)
        for url in parser.urls:
            parsed = urlsplit(url)
            if parsed.scheme in ('mailto', 'tel', 'data', 'javascript'):
                continue
            if parsed.netloc and parsed.netloc != 'yzll0.github.io':
                continue
            path = unquote(parsed.path)
            if not path:
                continue
            target = SITE / path.lstrip('/') if path.startswith('/') else page.parent / path
            if target.is_dir():
                target /= 'index.html'
            count += 1
            if not target.exists():
                errors.append(f'Broken link: {page.relative_to(SITE)} -> {url}')
    for path in SITE.rglob('*'):
        if path.name == 'CV.pdf' or path.name.startswith('codex_homepage_cv_prompt'):
            errors.append(f'Private reference input published: {path.relative_to(SITE)}')
    for directory in ['scripts', 'tmp', '.venv', 'vendor', 'markdown_generator', 'talkmap']:
        if (SITE / directory).exists():
            errors.append(f'Development directory published: {directory}')
    sitemap = (SITE / 'sitemap.xml').read_text()
    for path in ['https://yzll0.github.io' + url for pair in PAGE_PAIRS for url in pair]:
        if f'<loc>{path}</loc>' not in sitemap:
            errors.append(f'Sitemap missing {path}')
    check_bilingual(errors)
    if errors:
        raise SystemExit('\n'.join(sorted(set(errors))))
    print(f'Checked {count} local links/assets; six bilingual pages and both PDFs passed; no template content or private inputs in site output.')


if __name__ == '__main__':
    main()
