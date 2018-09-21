.PHONY: all clean init test

init:
	pre-commit install
	pre-commit install -t commit-msg
	pipenv install --dev

test:
	pipenv run tox
