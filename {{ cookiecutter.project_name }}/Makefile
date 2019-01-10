.PHONY: all clean init test formatting

init:
	poetry install

test:
	poetry run tox

formatting:
	poetry run tox -e formatting
