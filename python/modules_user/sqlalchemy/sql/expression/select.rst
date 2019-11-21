.. title:: python sqlalchemy expression select

.. meta::
    :description:
        Справочная информация по python модулю sqlalchemy, .sql.expression.select.
    :keywords:
        python sqlalchemy expression select

.. py:currentmodule:: sqlalchemy.sql.expression

select
======

select()
--------

Возвращает объект :py:class:`Select`

.. code-block:: py

    select_stmt = select([user_table])
    conn.execute(select_stmt).fetchall()


Select()
--------

.. py:class:: Select()

    .. code-block:: py

        stmt = select([user_table])
        # select user.id from "user"

        connection.execute(stmt)


    .. py:method:: order_by()

        .. code-block:: py

            stmt.order_by(user_table.c.username)
            '''
            select
                user.id
            from
                "user"
            order by
                user.username
            '''


    .. py:method:: select_from()

        .. code-block:: py

            (
                select([user_table, address_table])
                .select_from(
                    user_table.join(address_table)
                )
            )


    .. py:method:: where()

        .. code-block:: py

            stmt.where(user_table.c.username == 'ilnurgi')
            '''
            select
                user.id
            from
                "user"
            where
                user.username = 'ilnurgi'
            '''

        .. code-block:: py

            stmt.where(
                or_(
                    user_table.c.username == 'ilnurgi',
                    user_table.c.username == 'ilnurgi1',
                )
            )
            '''
            select
                user.id
            from
                "user"
            where
                user.username = 'ilnurgi'
                or
                user.username = 'ilnurgi1'
            '''

        .. code-block:: py

            (
                stmt
                .where(user_table.c.username == 'ilnurgi')
                .where(user_table.c.fullname == 'ilnurgi1')
            )
            '''
            select
                user.id
            from
                "user"
            where
                user.username = 'ilnurgi'
                and
                user.fullname = 'ilnurgi1'
            '''

