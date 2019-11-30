.. title:: python sqlalchemy connection

.. meta::
    :description:
        Справочная информация по python модулю sqlalchemy.engine.Connection.
    :keywords:
        python sqlalchemy connection

.. py:currentmodule:: sqlalchemy.engine

Connection
==========

.. py:class:: Connection()

    Объект соединения с базой

    .. code-block:: py

        conn = engine.connection()


    .. py:method:: begin()

        Создает транзакцию и возвращает её, :py:class:`sqlalchemy.engine.Transaction()`


    .. py:method:: close()

        Закрывает соединение с базой

        .. code-block:: py

            conn.close()


    .. py:method:: execute()

        Выполняет запрос в базу и возвращает :py:class:`sqlalchemy.engine.ResultProxy()`

        .. code-block:: py

            result = conn.execute(sql)
            result = conn.execute(
                'select * from post where id=:post_id',
                post_id=1,
            )

            conn.execute(
                user_table.insert(),
                [
                    {
                        'username': 'ilnurgi'
                    }
                ]
            )
