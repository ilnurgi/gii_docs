.. title:: psycopg2.cursor

.. meta::
    :description: psycopg2.cursor
    :keywords: 
        python psycopg2 cursor, 
        postgres psycopg2 cursor, 
        psycopg2 cursor

.. py:module:: psycopg2

cursor
======

.. py:class:: cursor()

    Объект курсор

    Поддерживает интерфейс контекстного менеджера

    .. code-block:: py

        with psycopg2.connection() as connection:
            with connection.cursor() as cursor:
                pass

    .. code-block:: py

        cur.execute("SELECT * FROM test;")
        for record in cur:
           print(record)

        # (1, 100, "abc'def")
        # (2, None, 'dada')
        # (3, 42, 'bar')


    .. py:attribute:: arraysize


    .. py:attribute:: closed


    .. py:attribute:: connection

        :py:class:`psycopg2.connection()` ссылка на объект соединения с БД, 
        к которому этот курсор относится


    .. py:attribute:: descriptions

        :py:class:`psycopg2.extensions.Column()` описание одного поля результата

    
    .. py:attribute:: itersize


    .. py:attribute:: lastrowid


    .. py:attribute:: name

        Имя курсора, если он был задан во время создания


    .. py:attribute:: query

        Строка последнего выполненого запроса

        .. code-block:: py

            cursor.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (42, 'bar'))
            cursor.query
            # "INSERT INTO test (num, data) VALUES (42, E'bar')"


    .. py:attribute:: rowcount


    .. py:attribute:: rownumber


    .. py:attribute:: scrollable


    .. py:attribute:: statusmessage

        .. code-block:: py
            
            cursor.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (42, 'bar'))
            cursor.statusmessage
            # 'INSERT 0 1'
    

    .. py:attribute:: tzinfo_factory


    .. py:attribute:: withhold


    .. py:method:: callproc(procname, parameters)


    .. py:method:: cast(oid, s)

        Преобразует значение из базы в питон объект


    .. py:method:: close()

        Закрывает курсор


    .. py:method:: copy_expert(sql, file, size=8192)

        .. code-block:: py

            cur.copy_expert("COPY test TO STDOUT WITH CSV HEADER", sys.stdout)
            """
            id,num,data
            1,100,abc'def
            2,,dada
            ...
            """


    .. py:method:: copy_from(file, table, sep='\t', null='\\N', size=8192, colums=None)

        Загружает данные из файлового объекта в таблицу

        .. code-block:: py

            f = StringIO("42\tfoo\n74\tbar\n")
            cur.copy_from(f, 'test', columns=('num', 'data'))
            cur.execute("select * from test where id > 5;")
            cur.fetchall()
            # [(6, 42, 'foo'), (7, 74, 'bar')]


    .. py:method:: copy_to(file, table, sep='\t', null='\\N', columns=None)

        Выгружает данные из таблицы в файловый объект

        .. code-block:: py

            cursor.copy_to(sys.stdout, 'test', sep="|")
            """
            1|100|abc'def
            2|\N|dada
            ...
            """


    .. py:method:: execute(query, vars=None)

        Выполняет указанный запрос

        .. code-block:: py

            cursor.execute(
                'SELECT * FROM airport WHERE city_code = %s', 
                ('ALA', )
            )

            cursor.execute(
                'SELECT * FROM engine_airport WHERE city_code = %(city_code)s',
               {'city_code': 'ALA'}
           )

       .. code-block:: py

            from psycopg2 import sql

            cur.execute(
                sql.SQL("insert into {} values (%s, %s)").format(sql.Identifier('my_table')),
                [10, 20]
            )

        .. code-block:: py

            with conn.cursor() as cursor:
                columns = ('country_name', 'airport_name')
                stmt = (
                    sql.SQL('SELECT {} FROM {} LIMIT 5')
                        .format(
                            sql.SQL(',').join(map(sql.Identifier, columns)),
                            sql.Identifier('airport'))
                )
                cursor.execute(stmt)

                for row in cursor:
                    print(row)

            ('Россия', 'Аэропорт')
            ...
    

    .. py:method:: executemany(query, vars=None)
    

    .. py:method:: fetchall()

        Возвращает все оставшиеся записи

        .. code-block:: py

            cursor.execute("SELECT * FROM test;")
            cursor.fetchall()
            # [(1, 100, "abc'def"), (2, None, 'dada'), (3, 42, 'bar')]


    .. py:method:: fetchmany(size=cursor.size)

        Возвращает указанное количесвто записей, по умолчанию - все

        .. code-block:: py

            cur.execute("SELECT * FROM test;")
            
            cur.fetchmany(2)
            # [(1, 100, "abc'def"), (2, None, 'dada')]
            
            cur.fetchmany(2)
            # [(3, 42, 'bar')]
            
            cur.fetchmany(2)
            # []


    .. py:method:: fetchone()

        Возвращает одну запись

        .. code-block:: py

            cursor.execute("SELECT * FROM test WHERE id = %s", (3,))
            cursor.fetchone()
            # (3, 42, 'bar')


    .. py:method:: mogrify(operation, params)

        .. code-block:: py

            cursor.mogrify("INSERT INTO test (num, data) VALUES (%s, %s)", (42, 'bar'))
            # "INSERT INTO test (num, data) VALUES (42, E'bar')"


    .. py:method:: scroll(value, mode='relative')

        Переместить курсор на указанную позицию


    .. py:method:: setinputsizes(sizes)
    
    .. py:method:: setoutputsizes(sizes, column)
