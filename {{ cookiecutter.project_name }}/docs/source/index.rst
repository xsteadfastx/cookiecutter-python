{{ cookiecutter.project_name }}
{% for char in range(cookiecutter.project_name|length) %}={% endfor %}

{{ cookiecutter.project_short_description }}

.. mdinclude:: ../../CHANGELOG.md

.. include:: modules.rst

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
