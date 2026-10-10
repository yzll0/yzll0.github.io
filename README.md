# Weixuan Yuan's academic homepage

AcademicPages/Jekyll website for `yzll0.github.io`. Keep the existing theme and GitHub Pages build model.

## Content

- `_pages/about.md`: biography and selected research.
- `_pages/publications.md`: selected published papers, followed by the under-review manuscript.
- `_pages/cv.md`: **the only manually maintained source of CV content**, shared by `/cv/` and the PDF.
- `_data/navigation.yml`: navigation; `_config.yml`: identity, contact details, collections, and build exclusions.
- `scripts/cv.css`: PDF typography only; `assets/css/profile.css`: small website reading adjustments.

## Rebuild the CV (no LaTeX)

Python 3.10+ and Chrome or Playwright Chromium are sufficient. First-time setup:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r scripts/requirements-cv.txt
```

On macOS, the builder automatically uses an installed Google Chrome with a fresh temporary profile. Otherwise, install the browser once:

```sh
.venv/bin/python -m playwright install chromium
```

On Linux, Playwright may also require system browser libraries (`playwright install --with-deps chromium`). An alternative Chrome installation can be selected with `CV_CHROME_PATH=/absolute/path/to/chrome`.

After editing `_pages/cv.md`:

```sh
make cv
# Equivalent: .venv/bin/python scripts/build_cv.py
```

Output: `files/Weixuan_Yuan_CV.pdf`. The script removes YAML front matter, renders the remaining Markdown/HTML, hides the web download controls in print, and generates a searchable A4 PDF with clickable links and page numbers. Rendering makes no network requests. It checks for 1–2 pages and extractable text before replacing the output. Keep the body free of Liquid template tags; use portable Markdown and small HTML elements for dates and print pagination.

To generate page images for visual review, install Poppler (`pdftoppm`) and run:

```sh
make cv-preview
```

Review **every** `tmp/pdfs/cv-page-*.png` after content/layout changes. The HTML preview is `tmp/pdfs/Weixuan_Yuan_CV.html`. All preview files are ignored by Git and excluded from Jekyll.

## Build and preview the website

Use a current Ruby (3.1+ recommended) and Bundler. If using a custom bundle directory, choose a path without `:` (the checkout name `CV:page` is incompatible with Bundler's `vendor/bundle` path). Keep dependencies outside the checkout in that case:

```sh
bundle config set --local path /tmp/weixuan-jekyll-bundle
bundle install
bundle exec jekyll build
bundle exec jekyll serve --host 127.0.0.1
```

Open `http://127.0.0.1:4000/`. After a build, run `python3 scripts/check_site.py` to verify local links, sitemap entries, template cleanup, and reference-input exclusions. `make site` is an alias for the build. The generated `_site/` is ignored. Jekyll's sitemap plugin generates `sitemap.xml`; there is no hand-maintained sitemap. GitHub Pages does not regenerate the CV PDF: rebuild it locally whenever its Markdown changes.

## Publication review before any commit or push

**This local draft contains unpublished AuXSpec material** in the homepage, publications page, CV source, and generated PDF. Publishing any of these to this public repository associates Weixuan Yuan with the ICLR 2027 submission. Review the anonymity/publication policy and the co-first-author wording before publishing. No unpublished collaborator names, manuscript PDF, or private source code are included.

The old root-level `CV.pdf` and the task prompt are private reference inputs: they are ignored by Git and explicitly excluded from the Jekyll output. These exclusions do not protect files already committed or manually force-added. Check the complete staged diff before any future publication.

Pending personal checks: AuXSpec disclosure and co-first-author wording; whether there is enough completed hands-on training work to list PyTorch (currently omitted); the contact email `weixuan.yuan@inf.ethz.ch`.

## Source verification (10 October 2026)

- [arXiv](https://arxiv.org/abs/2507.20354): FOCS paper title, all eight authors, deterministic almost-linear running time.
- [FOCS slides](https://ywwywwyww.github.io/files/DeterGHTreeSlides.pdf): accessible PDF; matching title, authors, and FOCS 2025 label. The fact that Weixuan presented is supplied by the owner.
- [Springer publisher page](https://link.springer.com/article/10.1007/s11425-023-2343-7): PCA paper, 2025, author order; Xuehu Zhu and Weixuan Yuan share the equal-contribution author note.
- [Wiley publisher page](https://onlinelibrary.wiley.com/doi/10.1111/sjos.70052): dimension-reduction paper, 2026, author order; Xinru Jia and Weixuan Yuan contributed equally.
- [ETH announcement](https://inf.ethz.ch/news-and-events/spotlights/infk-news-channel/2025/09/eth-medals-and-willi-studer-prizes-for-masters-graduates.html): Willi Studer Prize 2025, best Data Science Master's graduate (not an ETH Medal).

Education dates, GPA, teaching, research contributions, and unpublished AuXSpec results follow the owner's updated fact sheet. The older CV is reference material only. No withdrawn papers are included.

## Theme

Based on [AcademicPages](https://github.com/academicpages/academicpages.github.io), derived from Minimal Mistakes. See `LICENSE`.
