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

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('href', 'src') and value:
                self.urls.append(value)


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
    for path in ['https://yzll0.github.io/', 'https://yzll0.github.io/publications/', 'https://yzll0.github.io/cv/']:
        if f'<loc>{path}</loc>' not in sitemap:
            errors.append(f'Sitemap missing {path}')
    for removed in ['zh', 'files/Weixuan_Yuan_CV_zh.pdf']:
        if (SITE / removed).exists():
            errors.append(f'Removed Chinese content still published: {removed}')
    pdf = SITE / 'files/Weixuan_Yuan_CV.pdf'
    if not pdf.exists() or pdf.read_bytes() != (ROOT / 'files/Weixuan_Yuan_CV.pdf').read_bytes():
        errors.append('English CV PDF missing or stale.')
    if errors:
        raise SystemExit('\n'.join(sorted(set(errors))))
    print(f'Checked {count} local links/assets; no template content or private inputs in site output.')


if __name__ == '__main__':
    main()
