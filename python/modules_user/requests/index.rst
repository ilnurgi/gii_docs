.. title:: python requests

.. meta::
    :description:
        Справочная информация по python библиотеке requests.
        Библиотке для работы с сетевыми запросами.
    :keywords:
        python requests

.. py:module:: requests

requests
========

.. toctree::
    :maxdepth: 1

    adapters
    models

.. code-block:: sh

    $ pip install request


get()
-----

.. py:function:: get(url, params)

    Возвращает :py:class:`requests.models.Response`, результат запроса по урлу.

    .. code-block:: py

        response = requests.get('http://ilnurgi1.ru')

        response = requests.get(
            'http://ilnurgi1.ru',
            params={
                'q': 'ilnurgi'
            })

    .. code-block:: py

        response = requests.get('http://ilnurgi1.ru')
        response.text
        # some html text

    .. code-block:: py

        response = requests.get('http://ilnurgi1.ru/favicon.ico')
        
        with open('favicon.ico', 'wb') as f:
            f.write(response.content)


post()
------

.. py:function:: post(url, data)

    Возвращает :py:class:`requests.models.Response`, результат запроса по урлу.
    
    .. code-block:: py

        response = post(
            'ilnurgi.ru', 
            data={'id': 1}
        )


Session()
---------

.. py:class:: Session()

    Объект сессия, которая позволять переиспользовать соединения для нескольких запросов

    .. code-block:: py

        session = Session()
        session.get('http://ilnurgi.ru')

        adapter = HTTPAdapter(
            pool_connections=100,
            pool_maxsoze=100,
        )
        session.mount('htt://', adapter)