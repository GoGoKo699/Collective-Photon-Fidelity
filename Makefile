PYTHON ?= python3

.PHONY: all check

all: check

check:
	$(PYTHON) verification/check_fidelity.py
