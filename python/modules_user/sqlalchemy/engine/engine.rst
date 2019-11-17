.. title:: python sqlalchemy engine

.. meta::
    :description:
        Справочная информация по python модулю sqlalchemy.engine.Engine.
    :keywords:
        python sqlalchemy engine

.. py:currentmodule:: sqlalchemy.engine

Engine
======

.. py:class:: Engine(pool, dialect, url, logging_name=None, echo=None, execution_options=None, hide_parameters=False)

    .. code-block:: py

        engine = create_engine('sqlite:///:memory:')

    .. py:method:: begin()

        .. code-block:: py

            with engine.begin() as con:
                # выполняем запросы в одной транзакции
                con.execute(some sql)
                con.execute(some_sql)


    .. py:method:: connect()

        Создает объект соединения в базу и возвращает :py:class:`sqlalchemy.engine.Connection()`


    .. py:method:: execute(sql)

        Выполняет запрос в базу и возвращает :py:class:`sqlalchemy.engine.ResultProxy()`

        .. code-block:: py

            result = engine.execute(sql)
            
            result = engine.execute(
                'select * from post where id=:post_id', 
                post_id=1,
            )

            result = engine.execute(
                table.select().where(table.columns.username=='ilnurgi')
            )
