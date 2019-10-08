.PHONY: all clean init test formatting docs

init:
	poetry install

test:
	poetry run tox

formatting:
	poetry run tox -e formatting

docs:
	poetry run make -C docs/ html
