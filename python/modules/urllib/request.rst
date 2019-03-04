.. py:module:: request

request
=======


urlopen()
---------

.. py:method:: urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=None, context=None)

    Выполняет запрос и возвращает результат ответа с сервера
    в виде объекта :py:class:`http.client.HTTPResponse`

    .. code-block:: py

        conn = urlopen(url)

        conn = urlopen(Request(url))


Request()
---------

.. py:class:: Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)

    .. code-block:: py

        req = Request(url)

        req = Request(
            url, 
            data=urllib.parse.urlencode(query_args).encode('utf-8')
        )

    .. py:method:: add_header()
    
        .. code-block:: py

            req.add_header('User-agent', 'ChromeBrowser')