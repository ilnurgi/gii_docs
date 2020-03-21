.. title:: python urllib request

.. meta::
    :description:
        Справочная информация по python модулю urllib.request.
    :keywords:
        python urllib request

.. py:module:: urllib.request

request
=======


build_opener()
--------------

.. py:method:: build_opener([handler, ...])

    * **handler** - :py:class:`urllib.request.BaseHandler()`

    Возвращает объект для запросов :py:class:`urllib.request.OpenerDirector()`

    .. code-block:: py

        proxy_handler = urllib.request.ProxyHandler({'http': proxy_http_url})

        auth_handler = urllib.request.HTTPBasicAuthHandler()
        auth_handler.add_password(
            realm='Application',
            uri=uri,
            user=user,
            passwd=passwd
        )
        opener = urllib.request.build_opener(auth_handler, proxy_handler)
        urllib.request.install_opener(opener)
        urllib.request.urlopen(login_url)


getproxies()
------------

.. py:method:: getproxies()


install_opener()
----------------

.. py:method:: install_opener(opener)

    Устанавливает глобальный объект для запросов.

    Объектов может быть любой класс, реализующий методы :py:class:`urllib.request.OpenerDirector()`

    .. code-block:: py

        opener = urllib.request.build_opener(auth_handler)
        urllib.request.install_opener(opener)


pathname2url()
--------------

.. py:method:: pathname2url(path)


urlopen()
---------

.. py:method:: urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=None, context=None)

    Выполняет запрос и возвращает результат ответа с сервера
    в виде объекта :py:class:`http.client.HTTPResponse`

    .. code-block:: py

        conn = urlopen(url)

        conn = urlopen(Request(url))

        with urlopen(url) as f:
            print(f.read())
        # b'html content'

        req = Request(url=url, data=b'This data is passed to stdin of the CGI')
        with urllib.request.urlopen(req) as f:
            print(f.read().decode('utf-8'))
        Got Data: "This data is passed to stdin of the CGI"


url2pathname()
--------------

.. py:method:: url2pathname(path)


AbstractBasicAuthHandler()
--------------------------

.. py:class:: AbstractBasicAuthHandler()

    .. py:method:: http_error_auth_reqed(authreq, host, req, headers)


AbstractDigestAuthHandler()
---------------------------

.. py:class:: AbstractDigestAuthHandler()

    .. py:method:: http_error_auth_reqed(authreq, host, req, headers)

BaseHandler()
-------------

.. py:class:: BaseHandler()

    .. py:attribute:: add_parent
    .. py:method:: add_parent(director)
    .. py:method:: close()
    .. py:method:: default_open(req)
    .. py:method:: http_error_default(req, fp, code, msg, hdrs)
    .. py:method:: http_error_<nnn>>(req, fp, code, msg, hdrs)
    .. py:method:: unknown_open(req)
    .. py:method:: <protocol>_open(req)
    .. py:method:: <protocol>_request(req)
    .. py:method:: <protocol>_response(req, response)


CacheFTPHandler()
-----------------

.. py:class:: CacheFTPHandler()

    .. py:method:: setMaxConns(m)
    .. py:method:: setTimeout(t)


DataHandler()
-------------

.. py:class:: DataHandler()

    .. py:method:: data_open(req)

FileHandler()
-------------

.. py:class:: FileHandler()

    .. py:method:: file_open(req)


FTPHandler()
------------

.. py:class:: FTPHandler()

    .. py:method:: ftp_open(req)


HTTPBasicAuthHandler()
----------------------

.. py:class:: HTTPBasicAuthHandler(password_mgr=None)

    .. code-block:: py

        auth_handler = urllib.request.HTTPBasicAuthHandler()
        auth_handler.add_password(
            realm='Application',
            uri=uri,
            user=user,
            passwd=passwd
        )
        opener = urllib.request.build_opener(auth_handler)
        urllib.request.install_opener(opener)
        urllib.request.urlopen(login_url)

    .. py:method:: http_error_401(req, fp, code, msg, hdrs)


HTTPCookieProcessor()
---------------------

.. py:method:: HTTPCookieProcessor(cookijar=None)

    .. py:attribute:: cookiejar

        :py:class:`http.cookiejar.Cookiejar()`


HTTPDefaultErrorHandler()
-------------------------

.. py:class:: HTTPDefaultErrorHandler()


HTTPDigestAuthHandler()
-----------------------

.. py:class:: HTTPDigestAuthHandler(password_mgr=None)

    .. py:method:: http_error_401(req, fp, code, msg, hdrs)


HTTPErrorProcessor()
--------------------

.. py:class:: HTTPErrorProcessor()

    .. py:method:: http_response(request, response)
    .. py:method:: https_response(request, response)


HTTPHandler()
-------------

.. py:class:: HTTPHandler()

    .. py:method:: http_open(req)


HTTPPasswordMgr()
-----------------

.. py:class:: HTTPPasswordMgr()

    .. py:method:: add_password(realm, uri, user, passwd)
    .. py:method:: find_user_password(realm, aurhuri)


HTTPPasswordMgrWithDefaultRealm()
---------------------------------

.. py:class:: HTTPPasswordMgrWithDefaultRealm()

    .. py:method:: add_password(realm, uri, user, passwd)
    .. py:method:: find_user_password(realm, authuri)


HTTPPasswordMgrWithPriorAuth()
------------------------------

.. py:class:: HTTPPasswordMgrWithPriorAuth()

    .. py:method:: add_password(realm, uri, user, passwd, is_authenticated=False)
    .. py:method:: find_user_password(realm, authuri)
    .. py:method:: update_authenticated(self, uri, is_authenticated=False)
    .. py:method:: is_authenticated(self, authuri)


HTTPRedirectHandler()
---------------------

.. py:class:: HTTPRedirectHandler()

    .. py:method:: redirect_request(req, fp, code, msg, hdrs, newurl)
    .. py:method:: http_error_301(req, fp, code, msg, hdrs)
    .. py:method:: http_error_302(req, fp, code, msg, hdrs)
    .. py:method:: http_error_303(req, fp, code, msg, hdrs)
    .. py:method:: http_error_307(req, fp, code, msg, hdrs)


HTTPSHandler()
--------------

.. py:class:: HTTPSHandler()

    .. py:method:: https_open(req)

OpenerDirector()
----------------

.. py:class:: OpenerDirector()

    .. py:method:: add_handler(handler)
    .. py:method:: error(proto, *args)
    .. py:method:: open(url, data=None[, timeout])


ProxyBasicAuthHandler()
-----------------------

.. py:class:: ProxyBasicAuthHandler(password_mgr=None)

    .. py:method:: http_error_407(req, fp, code, msg, hdrs)


ProxyDigestAuthHandler()
------------------------

.. py:class:: ProxyDigestAuthHandler(password_mgr=None)

    .. py:method:: http_error_407(req, fp, code, msg, hdrs)


ProxyHandler()
--------------

.. py:class:: ProxyHandler()

    .. code-block:: py

        proxy_handler = urllib.request.ProxyHandler({'http': proxy_http_url})


    .. py:method:: <protocol>_open(req)


Request()
---------

.. py:class:: Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)

    * **url** - str
    * **data** - bytes

    .. code-block:: py

        query_args = {'q': 'text'}

        req = Request(url)

        req = Request(
            url,
            data=urllib.parse.urlencode(query_args).encode('utf-8')
        )


    .. py:attribute:: data
    .. py:attribute:: full_url
    .. py:attribute:: host
    .. py:attribute:: origin_req_host
    .. py:attribute:: selector
    .. py:attribute:: type
    .. py:attribute:: unverifiable

    .. py:method:: add_header(key, value)

        .. code-block:: py

            req.add_header('User-agent', 'ChromeBrowser')


    .. py:method:: add_unredirected_header()
    .. py:method:: get_full_url()
    .. py:method:: get_header(key, default=None)
    .. py:method:: get_method()
    .. py:method:: has_header(header)
    .. py:method:: header_items()
    .. py:method:: remove_header(header)
    .. py:method:: set_proxy(host, type)


UnknownHandler()
----------------

.. py:class:: UnknownHandler()

    .. py:method:: unknown_open()

