.. title:: python urllib3

.. meta::
    :description:
        Справочная информация по python модулю urllib3.
        Модуль для работы с сетевыми запросами.
    :keywords:
        python urllib3

.. py:module:: urllib3

urllib3
=======

.. code-block:: py

    import urllib3
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://www.google.com')
    print(r.data)

    import urllib3
    user_agent_header = urllib3.make_headers(user_agent="<USER AGENT>")
    pool = urllib3.ProxyManager(f'<PROXY IP>', headers=user_agent_header)
    r = pool.request('GET', 'https://www.google.com/')
