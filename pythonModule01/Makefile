VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

$(VENV):
	@python3 -m venv $(VENV)

install: $(VENV)
	$(PYTHON) -m pip install --upgrade pip
	$(PIP) install -r requiments.txt

allTasks: $(VENV)
	@for f in */*.py; do \
		$(PYTHON) $$f; \
	done

flakenorm: $(VENV)
	@if flake8 */*.py; then \
		echo "OK!!!"; \
	else \
		echo "Erro encontrado"; \
	fi

actulizeRequirements: $(VENV)
	$(PIP) freeze > requiments.txt