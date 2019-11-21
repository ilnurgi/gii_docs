.. title:: python sqlalchemy table

.. meta::

    :description:
        Справочная информация по python модулю sqlalchemy.schema.

    :keywords:
        python sqlalchemy table

.. py:currentmodule:: sqlalchemy.schema

Table
=====

.. py:class:: Table()

    .. code-block:: py

        meta = MetaData()

        table = Table(
            'user',
            meta,
            Column('id', Integer, primary_key=True),
            Column('profile_id', Integer),
            Column('version_id', Integer),
            ForeignKey('profile.id'),
            ForeignKeyConstraint(
                ['profile_id', 'version_id'],
                ['profile.profile_id', 'profile.version_id']
            ),
            # FOREIGN KEY(story_id, version_id) REFERENCES story (story_id, version_id)
        )

        # автозагрузка таблицы из базы
        table = Table('user', meta, autoload=True, autoload_with=engine)


    .. py:attribute:: columns

        Коллекция столбцов :py:class:`sqlalchemy.schema.Column()`

        .. code-block:: py

            table.c
            # <...ImmutableColumnCollection...>

            table.columns
            # <...ImmutableColumnCollection...>

            str(table.columns)
            # ['user.id', 'user.name']


    .. py:attribute:: name

        Название таблицы

        .. code-block:: py

            table.name
            # 'user'


    .. py:attribute:: primary_key

        Первичные ключи таблицы

        .. code-block:: py

            table.primary_key
            # PrimaryKeyConstraint(Column('id'))

            str(table.primary_key.columns)
            # ['user.id']

            table.primary_key.columns.id
            # Column('id', Integer())


    .. py:method:: create()

        .. code-block:: py

            table.create()
            # create table "user" ()


    .. py:method:: delete()

        .. code-block:: py

            table.delete()
            # delete from "user"


    .. py:method:: drop()

        .. code-block:: py

            table.drop(engine)
            # drop table "user"


    .. py:method:: join()

        .. code-block:: py

            user_table.join(
                address_table,
                user_table.c.id == address_table.c.user_id
            )
            # "user" join address on "user".id = address.user_id
            

    .. py:method:: insert()

        .. code-block:: py

            table.insert()
            # insert into "user" (id, name) values (:id, :name)

            insert_stmt = table.insert().values(username='ilnurgi')
            conn.execute(insert_stmt)


    .. py:method:: outerjoin()

    .. py:method:: select()

        .. code-block:: py

            table.select()
            # select * from "user"

    .. py:method:: update()

        .. code-block:: py

            table.update()
            # update "user" set id=:id, name=:name
