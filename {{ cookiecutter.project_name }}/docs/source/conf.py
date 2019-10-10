import os
import sys

sys.path.insert(0, os.path.abspath("../../src"))
project = "{{ cookiecutter.project_name }}"
copyright = "{% now 'utc', '%Y' %}, {{ cookiecutter.author_name }}"
author = "{{ cookiecutter.author_name }}"
release = "{{ cookiecutter.version }}"
extensions = [
    "m2r",
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_rtd_theme",
]
templates_path = ["_templates"]
exclude_patterns = []
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
