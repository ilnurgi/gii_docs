.. title:: psycopg2.sql

.. meta::
    :description: psycopg2.sql
    :keywords: 
        python psycopg2 sql, 
        postgres psycopg2 sql, 
        psycopg2 sql

.. py:module:: psycopg2.sql

sql
===

Composed()
----------

.. py:class:: Composed(seq)

    .. code-block:: py

        print(
            sql.Composed([sql.SQL("insert into "), sql.Identifier("table")])
                .as_string(conn)
        )
        # insert into "table"

    .. code-block:: py

        print(
            sql.Identifier('foo') + sql.Identifier('bar')  # a Composed
                .join(', ').as_string(conn)
        )
        # "foo", "bar"


Identifier()
------------

.. py:class:: Identifier(string)

    .. code-block:: py

        t1 = sql.Identifier("foo")
        t2 = sql.Identifier("ba'r")
        t3 = sql.Identifier('ba"z')
        
        print(sql.SQL(', ').join([t1, t2, t3]).as_string(conn))
        # "foo", "ba'r", "ba""z"

    .. code-block:: py

        print(
            sql.SQL("select {} from {}")
                .format(sql.Identifier("table", "field"), sql.Identifier("schema", "table"))
                .as_string(conn)
        )
        # select "table"."field" from "schema"."table"


Literal()
---------

.. py:class:: Literal(wrapped)

    .. code-block:: py

        s1 = sql.Literal("foo")
        s2 = sql.Literal("ba'r")
        s3 = sql.Literal(42)
        print(sql.SQL(', ').join([s1, s2, s3]).as_string(conn))
        # 'foo', 'ba''r', 42


Placeholder()
-------------

.. py:class:: Placeholder(name=None)

    .. code-block:: py

        names = ['foo', 'bar', 'baz']

        print(
            sql.SQL("insert into table ({}) values ({})")
            .format(
                sql.SQL(', ').join(map(sql.Identifier, names)),
                sql.SQL(', ').join(sql.Placeholder() * len(names)))
            .as_string()
        )
        # insert into table ("foo", "bar", "baz") values (%s, %s, %s)

        print(
            sql.SQL("insert into table ({}) values ({})")
                .format(
                    sql.SQL(', ').join(map(sql.Identifier, names)),
                    sql.SQL(', ').join(map(sql.Placeholder, names)))
                .as_string()
        )
        # insert into table ("foo", "bar", "baz") values (%(foo)s, %(bar)s, %(baz)s)


SQL()
-----

.. py:class:: SQL(string)

    .. code-block:: py

        query = sql.SQL("select {0} from {1}").format(
            sql.SQL(', ').join([sql.Identifier('foo'), sql.Identifier('bar')]),
            sql.Identifier('table'))
        query.as_string(conn)
        # select "foo", "bar" from "table"


    .. py:attribute:: string


    .. py:method:: format(*args, **kwargs)

        .. code-block:: py

            print(
                sql.SQL("select * from {} where {} = %s")
                    .format(sql.Identifier('people'), sql.Identifier('id'))
                    .as_string(conn)
            )
            # select * from "people" where "id" = %s

            print(
                sql.SQL("select * from {tbl} where {pkey} = %s")
                    .format(tbl=sql.Identifier('people'), pkey=sql.Identifier('id'))
                    .as_string(conn)
            )
            # select * from "people" where "id" = %s


    .. py:method:: join(seq)

        .. code-block:: py

            prin(
                sql.SQL(', ')
                    .join(sql.Identifier(n) for n in ['foo', 'bar', 'baz'])
                    .as_string(conn)
            )
            # "foo", "bar", "baz"