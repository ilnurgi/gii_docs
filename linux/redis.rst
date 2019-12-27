.. title:: redis

.. meta::
    :description:
        Справочная информация по сервису redis, хранилище ключ-значение
    :keywords:
        redis

.. py:module:: redis

redis
=====

https://redis.io/

.. code-block:: sh

    $ apt-get install redis-server

.. code-block:: sh

    $ redis-cli --version
    redis-cli 5.0.3

    $ redis-cli

    127.0.0.1:6379> keys *
    (empty list or set)

    127.0.0.1:6379> ping
    pong

    127.0.0.1:6379> set bahamas nassau
    ok

    127.0.0.1:6379> get japan
    (nil)

    127.0.0.1:6379> get bahamas
    "nassau"

    127.0.0.1:6379> mset bahamas nassau norway oslo
    ok

    127.0.0.1:6379> mget bahamas norway
    1) nassau
    2) oslo

    127.0.0.1:6379> exists bahamas
    (integer) 1

    127.0.0.1:6379> exists sweden
    (integer) 0

    127.0.0.1:6379> hset ilnurgi_site url "http://ilnurgi.ru"
    (integer) 1


FLUSHDB
-------

Очистка базы данных

.. code-block:: sh

    127.0.0.1:6379> FLUSHDB
    OK


Множества
---------
SADD
----

SCARD
-----

SDIFF
-----

SDIFFSTORE
----------

SINTER
------

SINTERSTORE
-----------

SISMEMBER
---------

SMEMBERS
--------

SMOVE
-----

SPOP
----

SRANDMEMBER
-----------

SREM
----

SSCAN
-----

SUNION
------

SUNIONSTORE
-----------


Хеши
----

HDEL
----

HEXISTS
-------

HGET
-----

HGETALL
----------

HINCRBY
-------

HINCRBYFLOAT
------------

HKEYS
-----

HLEN
----

HMGET
-----

HMSET
-----

HSCAN
-----

HSET
----

HSETNX
------

HSTRLEN
-------

HVALS
-----


Списки
---------

BLPOP
-----

BRPOP
-----

BRPOPLPUSH
----------

LINDEX
------

LINSERT
-------

LLEN
----

LPOP
----

LPUSH
-----

LPUSHX
------

LRANGE
------

LREM
----

LSET
----

LTRIM
-----

RPOP
----

RPOPLPUSH
---------

RPUSH
-----

RPUSHX
------


Строки
------

APPEND
------

BITCOUNT
--------

BITFIELD
--------

BITOP
----------

BITPOS
------

DECR
----

DECRBY
------

GET
---

GETBIT
------

GETRANGE
--------

GETSET
------

INCR
----

INCRBY
------

INCRBYFLOAT
-----------

MGET
----

MSET
----

MSETNX
------

PSETEX
------

SET
---

SETBIT
------

SETEX
-----

SETNX
-----

SETRANGE
--------

STRLEN
------
