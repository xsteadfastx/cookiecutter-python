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
    assert "poetry run flake8 {toxinidir}/src/my_python_project/" in tox_ini


def test_hook_git(created_project):
    with open(created_project.joinpath(".git/config")) as f:
        config = f.read()

    assert "name = Don Draper" in config
    assert "email = draper@sterling-cooper-draper-pryce.tld" in config


def test_travis(created_project):
    with open(created_project.joinpath(".travis.yml")) as f:
        travis_yml = f.read()

    assert "TOXENV=py" in travis_yml
    assert "TOXENV=flake8" in travis_yml
    assert "TOXENV=pylint" in travis_yml
    assert "TOXENV=mypy" in travis_yml
    assert "TOXENV=black-only-check" in travis_yml
    assert (
        "docker build -t my_python_project-tests " "-f Dockerfile.tests ."
    ) in travis_yml
    assert (
        "docker run --rm -t -v $PWD:/data -w /data "
        "-e TOX_WORK_DIR=/tmp "
        "my_python_project-tests tox -v -e $TOXENV"
    ) in travis_yml
