PYTHON ?= .venv/bin/python

.PHONY: cv cv-en cv-zh cv-preview site
cv:
	$(PYTHON) scripts/build_cv.py

cv-en:
	$(PYTHON) scripts/build_cv.py --lang en

cv-zh:
	$(PYTHON) scripts/build_cv.py --lang zh

cv-preview:
	$(PYTHON) scripts/build_cv.py --preview

site:
	bundle exec jekyll build
