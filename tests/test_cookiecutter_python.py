# pylint: disable=missing-docstring,redefined-outer-name,invalid-name
from pathlib import Path

import pytest
from cookiecutter.main import cookiecutter


@pytest.fixture
def created_project(tmpdir):
    proj_dir = tmpdir.strpath
    cookie_dir = str(Path(__file__).resolve().parents[1])
    cookiecutter(cookie_dir, no_input=True, output_dir=proj_dir)

    yield Path(proj_dir).joinpath("my_python_project")


def test_tox(created_project):
    with open(created_project.joinpath("tox.ini")) as f:
        tox_ini = f.read()

    assert "poetry run pytest --cov=my_python_project" in tox_ini
    assert "poetry run codecov" in tox_ini
    assert "poetry run bandit" in tox_ini
    assert "poetry run prospector" in tox_ini


def test_hook_git(created_project):
    with open(created_project.joinpath(".git/config")) as f:
        config = f.read()

    assert "name = Don Draper" in config
    assert "email = draper@sterling-cooper-draper-pryce.tld" in config


def test_travis(created_project):
    with open(created_project.joinpath(".travis.yml")) as f:
        travis_yml = f.read()

    assert "TOXENV=py37" in travis_yml
    assert "TOXENV=prospector" in travis_yml
    assert "TOXENV=bandit" in travis_yml
    assert "TOXENV=mypy" in travis_yml
    assert "TOXENV=black-only-check" in travis_yml
    assert "docker run --rm -t" in travis_yml
    assert "-v $PWD:/data" in travis_yml
    assert "-w /data" in travis_yml
    assert "-e TOX_WORK_DIR=/tmp" in travis_yml
    assert "-e CI" in travis_yml
    assert "-e TRAVIS" in travis_yml
    assert "-e SHIPPABLE" in travis_yml
    assert "-e TRAVIS_BRANCH" in travis_yml
    assert "-e TRAVIS_COMMIT" in travis_yml
    assert "-e TRAVIS_JOB_NUMBER" in travis_yml
    assert "-e TRAVIS_PULL_REQUEST" in travis_yml
    assert "-e TRAVIS_JOB_ID" in travis_yml
    assert "-e TRAVIS_REPO_SLUG" in travis_yml
    assert "-e TRAVIS_TAG" in travis_yml
    assert "-e TRAVIS_OS_NAME" in travis_yml
    assert (
        "xsteadfastx/tox-python:minimal /bin/sh -c "
        '"sudo apk add --no-cache gcc musl-dev; tox -v -e $TOXENV"'
    ) in travis_yml
