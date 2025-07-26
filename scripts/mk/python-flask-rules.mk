# TODO Update this variable
MODULE ?= my_service

.PHONY: all
all: format lint doc test

.PHONY: deps
deps: .venv  ## Install dependencies in a python virtual environment
	source .venv/bin/activate; pip install -U pip
	source .venv/bin/activate; pip install poetry
	source .venv/bin/activate; python3 -m poetry install --no-root --all-extras --all-groups

.venv:
	python3 -m venv .venv

.PHONY: format
format: .venv   ## Apply format rules to the python code
	source .venv/bin/activate; black "${MODULE}"
	source .venv/bin/activate; black tests

.PHONY: lint
lint: .venv  ## Run linter on the python code
	source .venv/bin/activate; pylint "${MODULE}"

.PHONY: run
run: .venv  ## Execute hello_world
	source .venv/bin/activate; python3 -m "${MODULE}"

.PHONY: debug
debug: .venv  ## Run PDB debugger
	source .venv/bin/activate; python3 -m pdb -m "$(MODULE)"

.PHONY: test
test: .venv  ## Run tests
	source .venv/bin/activate; python3 -m pytest

.PHONY: test-cov
test-cov: .venv  ## Get coverage report
	source .venv/bin/activate; python3 -m \
	  pytest --cov=${MODULE}

.PHONY: doc
doc: .venv  ## Generate documentation from the source code
	# TODO Update your module name
	source .venv/bin/activate; pdoc3 --force -o docs/ "${MODULE}"

.PHONY: clean
clean:
	# rm -rf .venv
	# find . -iname __pycache__ | xargs rm -rf 
