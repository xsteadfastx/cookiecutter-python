.PHONY: all clean init test formatting docs shiv

init:
	poetry install

test:
	poetry run tox

formatting:
	poetry run tox -e formatting

docs:
	poetry run tox -e docs

shiv:
	mkdir -p dist/
	poetry run tox -e shiv
