# pylint: disable=missing-docstring
import re

from setuptools import setup

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

with open("src/{{ cookiecutter.project_name }}/__init__.py", "r") as f:
    VERSION_MATCH = re.search(r"__version__ = \"(.*?)\"", f.read())
    if VERSION_MATCH:
        VERSION = VERSION_MATCH.group(1)

setup(
    name="{{ cookiecutter.project_name }}",
    version=VERSION,
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",
    description="{{ cookiecutter.project_short_description }}",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=["{{ cookiecutter.project_name }}"],
    package_dir={"": "src"},
    package_data={},
    include_package_data=True,
    install_requires=[
        "Click",
    ],
    entry_points="""
        [console_scripts]
        {{ cookiecutter.project_name }}={{ cookiecutter.project_name }}.cli:main
    """
)
