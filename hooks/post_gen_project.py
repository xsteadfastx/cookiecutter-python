"""Post project creation hook."""
import os
import subprocess
import sys
from distutils.version import StrictVersion

# init git
subprocess.run(["git", "init"], check=True)
subprocess.run(
    ["git", "config", "--add", "user.name", "{{ cookiecutter.author_name }}"],
    check=True,
)
subprocess.run(
    ["git", "config", "--add", "user.email", "{{ cookiecutter.author_email }}"],
    check=True,
)

# install deps through poetry
DEPS = ["click"]
DEV_DEPS = [
    "bandit",
    "codecov",
    "isort",
    "mypy",
    "prospector",
    "pytest",
    "pytest-cov",
    "tox",
]

subprocess.run(["poetry", "add"] + DEPS, check=True)
subprocess.run(["poetry", "add", "--dev"] + DEV_DEPS, check=True)
if StrictVersion("{{ cookiecutter.python_version }}") >= StrictVersion("3.6"):
    subprocess.run(["poetry", "add", "--dev", "black==19.10b0"], check=True)

# remove .python-version file
if os.path.exists(".python-version"):
    os.remove(".python-version")
if os.path.exists(".python-version"):
    sys.exit(1)
