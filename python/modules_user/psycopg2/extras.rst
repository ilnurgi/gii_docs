.. title:: psycopg2.extras

.. meta::
    :description: psycopg2.extras
    :keywords: 
        python psycopg2 extras, 
        postgres psycopg2 extras, 
        psycopg2 connection

.. py:module:: psycopg2.extras

extras
======

DictConnection()
----------------

.. py:class:: DictConnection()


DictCursor()
------------

.. py:class:: DictCursor()


LoggingConnection()
-------------------

.. py:class:: LoggingConnection()

    .. py:method:: filter(msg, curs)

        Фильтрует вывод в лог


    .. py:method:: initialize(logobj, mintime=0)

        Инициализирует логгер


LoggingCursor()
---------------

.. py:class:: LoggingCursor()


MinTimeLoggingConnection()
--------------------------

.. py:class:: MinTimeLoggingConnection()


MinTimeLoggingCursor()
----------------------

.. py:class:: MinTimeLoggingCursor()

    .. py:method:: filter(msg, curs)

        Фильтрует вывод в лог


    .. py:method:: initialize(logobj, mintime=0)

        Инициализирует логгер


NamedTupleConnection()
----------------------

.. py:class:: NamedTupleConnection()


NamedTupleCursor()
------------------

.. py:class:: NamedTupleCursor()