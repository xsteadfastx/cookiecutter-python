"""Post project creation hook."""
import subprocess
import sys

RETURN_CODES = []

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

if any(RETURN_CODES):
    sys.exit(1)
