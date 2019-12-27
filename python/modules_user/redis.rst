.. title:: python redis

.. meta::
    :description:
        Справочная информация по python модулю redis
    :keywords:
        python redis

.. py:module:: redis

redis
=====

Клиент для подключения к серверу redis, сервер структуры данных

.. code-block:: shell

    pip install redis


.. code-block:: py

    import redis

    conn = redis.Redis()

    conn.set("key1", "value1")
    # True

.. code-block:: py

    redis_db = redis.StrictRedis(host=host, port=port, db=0)

    # список ключей в базе
    redis_db.keys()


Redis()
-------

.. py:class:: Redis(**kwargs)

    * **host** = localhost
    * **port** = 6397
    * **db** = 0
    * **password** = None
    * **socket_timeout** = None

    Объект для работы с базой данных

    .. py:method:: get(key)
    .. py:method:: set(key, value)
    .. py:method:: setex(key, expire_s, value)
    .. py:method:: psetex(key, expire_ms, value)

        Одиночное получение/установка данных

        .. code-block:: py

            conn.set('k1', 'v1')
            # True

            conn.get('k1')
            # b'v1'

            conn.setex('k2', timedelta(minutes=1), 'v2')
            # True
            # установка ключа со сроком годности


    .. py:method:: exists(key)

        Проверка на существование ключа

        .. code-block:: py

            con.exists('k3')
            # 0


    .. py:method:: expire(key, expire_s)
    .. py:method:: pexpire(key, expire_ms)

        Установка нового срока годности данных

        .. code-block:: py

            conn.expire('k1', timedelta(days=1))


    .. py:method:: hgetall(key)
    .. py:method:: hincrby(key, )

    .. py:method:: keys()

        Возвращает список всех ключей базы

        .. code-block:: py

            conn.keys()
            # [b'k1', b'k2']


    .. py:method:: mget(keys)
    .. py:method:: mset(data)

        Множественное получение/установка данных

        .. code-block:: py

            conn.mset({'k1': 'v1', 'k2': 'v2'})
            # True

            conn.mget(('k1', 'k2'))
            # [b'v1', b'v2']


    .. py:method:: persist(key)

        Удаляет срок годности данных

        .. code-block:: py

            con.persist('k1')


    .. py:method:: pipeline()

        Создает поток, для работы с данными.

        Т.е. обработать все данные за один запрос

        .. code-block:: py

            with conn.pipeline() as pipe:
                pipe.set('k1', 'v1')
                pipe.set('k2', 'v2')
                pipe.execute()


    .. py:method:: sadd(k, *values)
    .. py:method:: smembers(k)

        .. code-block:: py

            conn.sadd('k1', 'v1', 'v2')
            # 3

            conn.smembers('k1')
            # {b'v1', b'v2'}


    .. py:method:: ttl(key)
    .. py:method:: pttl(key)

        Возвращает срок годности данных по ключам в секндах/миллисекундах

        .. code-block:: py

            conn.ttl('k1')
            # 58

            conn.pttl('k1')
            # 57456


.. code-block:: py

    conn.set("key1", "value1")
    # True

    conn.get("key1")
    # "value1"

    conn.setnx("key1", "value1")
    # False
    # ключ уже существует

    conn.getset("key1", "new_value1")
    # value1
    # возвращает старое и сохраняет новое

    conn.getrange("key1", -6, -1)
    # "value1"

    conn.setrange("key1", 0, "NEW")

    conn.get("key1")
    # "NEW_value1"

    conn.mset({"key2": "value2"})
    # True

    conn.mget(("key1", "key2"))
    # ["NEW_value1", "value2"]

    conn.delete("fever")
    # True

    # время жизни ключа в секундах
    conn.expire("key1", 5)
    # True

    conn.ttl("key1")
    # 5

    # время истечения ключа
    conn.expireat("key1", 1233354354)


.. code-block:: py

    conn.set('key3', 0)

    conn.incr('key3')
    # 1

    conn.incr('key3', 10)
    # 11

    conn.decr('key3')
    # 10

    conn.decr('key3', 7)
    # 3

    conn.set('key4', '101.5')
    # True

    conn.incrbyfloat('key4')
    # 102.5

    conn.incrbyfloat('key4', 0.5)
    # 103.0

    conn.incrbyfloat('key4', -0.5)
    # 102.5


.. code-block:: py

    # списки могут содержать только строки

    conn.lpush('key5', 'value1')
    # 1

    conn.lpush('key5', 'value2', 'value3')
    # 3

    conn.linsert('key5', 'before', 'value2', 'value4')
    # 4

    conn.linsert('key5', 'after', 'value2', 'value5')
    # 5

    conn.lset('key5', 2, 'value6')
    # True

    conn.rpush('key5', 'value7')
    # 7

    conn.lindex('key5', 3)
    # 'value3'

    conn.lrange('key5', 0, 2)
    # 'value1', 'value2', 'value3'

    conn.ltrim('key5', 1, 4)
    # True

.. code-block:: py

    # хеши могут содержать только строки

    conn.hmset("key6", {"k1": "v1"})
    # True

    conn.hset("key6", "k1", "n_v1")
    # 1

    conn.hsetnx("key6", "k2", "v2")
    # 1

    conn.hget("key6", "k1")
    # "n_v1"

    conn.hmget("key6", "k1", "k2")
    # ["n_v1", "v2"]

    conn.hkeys("key6")
    # ["k1", "k2"]

    conn.hvals("key6")
    # ["n_v1", "v2"]

    conn.hlen("key6")
    # 2

    conn.hgetall("key6")
    # {"k1": "n_v1", "k2": "v2"}


.. code-block:: py

    conn.sadd("key11", "value1", "value2")
    # 2

    conn.scard("key11")
    # 2

    conn.smembers("key11")
    # {"value1", "value2"}

    conn.srem("key11", "value2")
    # True

    conn.sadd("key12", "value1", "value3")
    # 0

    # пересечение
    conn.sinter("key11", "key12")
    # {"value1"}

    # сохранение пересечения в переменную
    conn.sinterstore("key13", "key11", "key12")
    # 1

    conn.smembers("key13")
    # {"value1"}

    # объединение
    conn.sunion("key11", "key12")
    # {"value1", "value2", "value3"}

    # сохранение объединения в переменную
    conn.sunionstore("key14", "key11", "key12")
    # 3

    conn.sdiff("key11", "key12")
    # {"value3"}

    conn.sdiffstore("key15", "key11", "key12")
    # 1


.. code-block:: py

    # упорядоченные множества

    import time
    now = time.time()

    conn.zadd("key21", "value1", now)
    # 1

    conn.zadd("key21", "value2", now+(5*60))
    # 1

    conn.zadd("key21", "value3", now+(2*60*60))
    # 1

    conn.zadd("key21", "value4", now+(24*60*60))
    # 1

    conn.zrank("key21", "value3")
    # 2

    conn.zrange("key21", 0, -1)
    # ["value1", "value2", "value3", "value4"]

    conn.zrange("key21", 0, -1, withscores=True)
    # [("value1", 123456789), ...]


.. code-block:: py

    # биты

    conn.setbit("key41", "value1", 1)
    # 0

    conn.setbit("key41", "value2", 1)
    # 0

    conn.setbit("key42", "value1", 1)
    # 0

    conn.setbit("key43", "value1", 1)
    # 0

    conn.setbit("key43", "value3", 1)
    # 0

    conn.bitcount("key41")
    # 2

    conn.getbit("key42", "value3")
    # 0

    conn.bitop("and", "key44", "key41", "key42")
    # 542333

    conn.bitop("or", "key45", "key41", "key42")
    # 542332

    conn.bitcount("key44")
    # 3
