"""Post project creation hook."""
import os
import subprocess
import sys
from distutils.version import StrictVersion

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
DEPS = ["click"]

RETURN_CODES.append(subprocess.run(["poetry", "add"] + DEPS).returncode)

DEV_DEPS = [
    "codecov",
    "flake8",
    "isort",
    "mypy",
    "pylint",
    "pytest",
    "pytest-cov",
    "tox",
]

RETURN_CODES.append(subprocess.run(["poetry", "add", "--dev"] + DEV_DEPS).returncode)

if StrictVersion("{{ cookiecutter.python_version }}") >= StrictVersion("3.6"):
    RETURN_CODES.append(
        subprocess.run(["poetry", "add", "--dev", "black==19.3b0"]).returncode
    )

os.remove(".python-version")
if os.path.exists(".python-version"):
    sys.exit(1)

if any(RETURN_CODES):
    sys.exit(1)
