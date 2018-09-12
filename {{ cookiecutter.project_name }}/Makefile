.PHONY: init test

init:
	git init
	pre-commit install
	pre-commit install -t commit-msg
	pipenv install --dev

test:
	pipenv run tox
