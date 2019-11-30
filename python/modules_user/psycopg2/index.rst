.. title:: psycopg2

.. meta::
    :description: psycopg2
    :keywords: python psycopg2, postgres psycopg2, psycopg2

.. py:module:: psycopg2

psycopg2
========

.. code-block:: sh

    pip install psycopg2
    or
    pip install psycopg2-binary


.. toctree::
    :maxdepth: 1

    connection
    cursor
    exceptions
    extensions/index
    extras
    sql


apilevel
--------

.. py:attribute:: apilevel

    Возвращает версию DB API Level

    .. code-block:: py

        psycopg2.apilevel
        # '2.0'


threadsafety
------------

.. py:attribute:: threadsafety


paramstyle
----------

.. py:attribute:: paramstyle


connect()
---------

.. py:method:: connect(dsn=None, connection_factory=None, cursor_factory=None, async=False, **kwargs)

    Возвращает объект :py:class:`psycopg2.connection()`, подключение к БД

    .. code-block:: py

        con = psycopg2.connect('dbname=test user=postgres password=password')
        con = psycopg2.connect(
            dbname='test', 
            user='postgres', 
            password='password', 
            host='host', 
            port='port',
        )

    .. code-block:: py

        from psycopg2.extras import DictConnection, DictCursor

        dict_conn = connect('', connection_factory=DictConnection)

        dict_conn = connect('', cursor_factory=DictCursor)

