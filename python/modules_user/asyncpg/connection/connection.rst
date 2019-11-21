.. title:: python asyncpg connection

.. meta::
    :description: 
        Справочная информация по python библиотеке asyncpg.connection.Connection.
    :keywords: 
        python asynpg connection

.. py:currentmodule:: asyncpg.connection

Connection
==========

.. py:class:: Connection()

    .. code-block:: py

        conn = await asyncpg.connection(DSN)

    
    .. py:method:: fetch(sql)

        Возвращает список записей :py:class:`asyncpg.Record()`

        .. code-block:: py

            rows = conn.fetch('select * from "persons"')
            rows = conn.fetch('select * from "persons" where "id" = $1', 2)

    .. py:method:: transaction()

        .. code-block:: py

            async with conn.transaction():
                async conn.fetch()
