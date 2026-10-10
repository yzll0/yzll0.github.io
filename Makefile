PYTHON ?= .venv/bin/python

.PHONY: cv cv-preview site
cv:
	$(PYTHON) scripts/build_cv.py
cv-preview:
	$(PYTHON) scripts/build_cv.py --preview
site:
	bundle exec jekyll build
