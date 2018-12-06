.PHONY: all clean init test

init:
	pipenv lock
	pipenv install --dev

test:
	pipenv run tox
