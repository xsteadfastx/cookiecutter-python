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

    assert "pipenv run coverage run --source=my_python_project -m pytest" in tox_ini
    assert "pipenv run flake8 {toxinidir}/src/my_python_project/" in tox_ini


def test_hook_git(created_project):
    with open(created_project.joinpath(".git/config")) as f:
        config = f.read()

    assert "name = Don Draper" in config
    assert "email = draper@sterling-cooper-draper-pryce.tld" in config
