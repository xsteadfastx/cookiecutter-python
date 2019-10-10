.PHONY: all clean init test formatting docs

init:
	poetry install

test:
	poetry run tox

formatting:
	poetry run tox -e formatting

docs:
	poetry run sphinx-apidoc -f -M -o docs/source/ src/
	poetry run make -C docs/ html
