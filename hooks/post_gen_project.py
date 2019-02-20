"""Post project creation hook."""
import subprocess
import sys

RETURN_CODES = []

# init git
RETURN_CODES.append(subprocess.run(["git", "init"]).returncode)
RETURN_CODES.append(
    subprocess.run(
        ["git", "config", "--add", "user.name", "{{ cookiecutter.author_name }}"]
    ).returncode
)
RETURN_CODES.append(
    subprocess.run(
        ["git", "config", "--add", "user.email", "{{ cookiecutter.author_email }}"]
    ).returncode
)

# install deps through poetry
DEPS = [
    "click"
]

RETURN_CODES.append(
    subprocess.run(["poetry", "add"] + DEPS).returncode
)

DEV_DEPS = [
    "black==18.9b0",
    "codecov",
    "flake8",
    "isort",
    "mypy",
    "pylint",
    "pytest",
    "pytest-cov",
    "tox",
]

RETURN_CODES.append(
    subprocess.run(["poetry", "add", "--dev"] + DEV_DEPS).returncode
)

if any(RETURN_CODES):
    sys.exit(1)
