.. title:: python asyncpg

.. meta::
    :description:
        Справочная информация по python библиотеке asyncpg.
    :keywords:
        python asynpg

.. py:module:: asyncpg

asyncpg
=======

Асинхронный клиент для субд postgres

.. toctree::
    :maxdepth: 1

    connection/index
    record

connection()
------------

.. py:function:: connection()

    Возвращает объект соединения, :py:class:`asyncpg.connection.Connection()`

    .. code-block:: py

        conn = await connection('postgres://postgres:docsker@localhost/testdb')

create_pool()
-------------

.. py:function:: create_pool()

    .. code-block:: py

        pool = create_pool(DSN)
        async with pool.asquire() as conn:
            conn.fetch()