PYTHON ?= python3
LATEX ?= pdflatex
DOCUMENT := collective_photon_fidelity

.PHONY: all check pdf clean

all: check pdf

check:
	$(PYTHON) verification/check_fidelity.py

pdf:
	mkdir -p build
	cd theory && $(LATEX) -interaction=nonstopmode -halt-on-error -output-directory=../build $(DOCUMENT).tex
	cd theory && $(LATEX) -interaction=nonstopmode -halt-on-error -output-directory=../build $(DOCUMENT).tex
	cp build/$(DOCUMENT).pdf theory/$(DOCUMENT).pdf

clean:
	$(PYTHON) -c "import shutil; shutil.rmtree('build', ignore_errors=True)"
