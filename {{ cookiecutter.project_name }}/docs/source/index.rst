{{ cookiecutter.project_name }}
{% for char in range(cookiecutter.project_name|length) %}={% endfor %}


{{ cookiecutter.project_name}}.cli
{% for char in range(cookiecutter.project_name|length) %}-{% endfor %}----
.. automodule:: {{ cookiecutter.project_name }}.cli
   :members:

{{ cookiecutter.project_name}}.core
{% for char in range(cookiecutter.project_name|length) %}-{% endfor %}-----
.. automodule:: {{ cookiecutter.project_name }}.core
   :members:

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
