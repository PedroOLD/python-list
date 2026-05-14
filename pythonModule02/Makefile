VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip


$(VENV):
	python3 -m venv $(VENV)

install: $(VENV)
	$(PYTHON) -m pip install --upgrade pip
	$(PIP) install -r requeriments.txt

freeze: $(VENV)
	$(PIP) freeze > requeriments.txt

mypy: $(VENV)
	mypy */*.py

flakenorm: $(VENV)
	@if flake8 */*.py; then \
		echo "OK!!"; \
	else \
		echo "Error encontrado"; \
	fi

alltaks: $(VENV)
	@for f in */*.py; do \
		$(PYTHON) $$f; \
	done

