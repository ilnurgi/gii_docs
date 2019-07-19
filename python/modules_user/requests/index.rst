.. py:module:: requests

requests
========

.. toctree::
    :maxdepth: 1

    models

.. code-block:: shell

    pip install request


.. code-block:: py

    import requests
    response = requests.get("http://ilnurgi1.ru")
    response.text
    # some html text


get
---

.. py:function:: get(url: str) -> :py:class:`requests.models.Response`

    .. code-block:: py

        response = requests.get('http://ilnurgi1.ru')