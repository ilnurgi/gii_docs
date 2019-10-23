.. title:: python requests models

.. meta::
    :description: 
        Справочная информация по python библиотеке requests.models.
    :keywords: 
        python requests,
        python requests models

.. py:module:: requests.models

models
======

Response()
----------

.. py:class:: Response()


    .. py:attribute:: content

        .. code-block:: py

            with open('index.html', 'wb') as f:
                f.write(response.content)


    .. py:attribute:: headers

        .. code-block:: py

            response.headers
            # {'Content-Type': 'text/html; charset=utf-8'}


    .. py:attribute:: status_code

        .. code-block:: py

            response.status_code
            # 200


    .. py:attribute:: text

        .. code-block:: py

            response.text
            # '<!doctype html> ...'


    .. py:attribute:: url

        .. code-block:: py

            response.url
            # 'ilnurgi.ru?q=ilnurgi.ru'


    .. py:method:: json()

        Возвращает словарь, преобразованный из ответа в формате json.

        .. code-block:: py

            response.json()
            # {'q': 'ilnurgi.ru'}
