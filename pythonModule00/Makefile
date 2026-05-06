VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

$(VENV):
	python3 -m venv $(VENV)

install: $(VENV)
	$(PYTHON) -m pip install --upgrade pip
	$(PIP) install -r requirement.txt

alltask: $(VENV)
	@for f in */*.py; do \
		$(PYTHON) $$f; \
	done

actualize: $(VENV)
	$(PIP) freeze > requirement.txt

flakenorm: $(VENV)
	@if $(VENV)/bin/flake8	*/*.py; then \
		echo "OK!!"; \
	else \
		echo "Erro encontrado :/"; \
	fi