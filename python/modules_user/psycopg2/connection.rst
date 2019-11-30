.. title:: psycopg2.connection

.. meta::
    :description: psycopg2.connection
    :keywords: 
        python psycopg2 connection, 
        postgres psycopg2 connection, 
        psycopg2 connection

.. py:currentmodule:: psycopg2

connection
==========

.. py:class:: connection()

    Объект подключения к базе

    Поддерживает интерфейс контекстного менеджера

    .. code-block:: py

        with psycopg2.connection() as connection:
            pass


    .. py:method:: close()

        Закрывает соединение с базой

        .. code-block:: py

            connection.close()


    .. py:method:: commit()

        Фиксация изменений в транзакции

        .. code-block:: py

            connection.commit()


    .. py:method:: cursor(name=None, cursor_factory=None, scrollable=None, withhold=False)

        Возвращает :py:class:`psycopg2.cursor`

        * cursor_factory - формат возвращаемых данных

            * :py:class:`psycopg2.extras.DictCursor` - поле базы будет в виде словаря
            * :py:class:`psycopg2.extras.NamedTupleCursor` - поле базы будет в виде именованного кортежа

        .. code-block:: py

            cur = connection.cursor()

        .. code-block:: py

            from psycopg2.extras import DictCursor, NamedTupleCursor

            cursor = connection.cursor(cursor_factory=DictCursor)
            ...
            row = cursor.fetchone()
            print(row)
            # {'id': 1, name: 'ilnurgi'}


    .. py:method:: rollback()

        Откат изменений в транзакции

        .. code-block:: py

            connection.rollback()
