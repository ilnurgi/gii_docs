.. title:: psycopg2.exceptions

.. meta::
    :description: psycopg2.exceptions
    :keywords: 
        python psycopg2 exceptions, 
        postgres psycopg2 exceptions, 
        psycopg2 exception

.. py:module:: psycopg2

exceptions
==========

Иерархия исключений:

 * StandartError

    - :py:class:`psycopg2.Warning`

    - :py:class:`psycopg2.Error`

        * :py:class:`psycopg2.InterfaceError`

        * :py:class:`psycopg2.DatabaseError`

            * :py:class:`psycopg2.DataError`

            * :py:class:`psycopg2.IntegrityError`

            * :py:class:`psycopg2.InternalError`

            * :py:class:`psycopg2.NotSupportedError`

            * :py:class:`psycopg2.OperationalError`

            * :py:class:`psycopg2.ProgrammingError`



DataError()
-----------

.. py:class:: DataError()


DatabaseError()
---------------

.. py:class:: DatabaseError()


Error()
-------

.. py:class:: Error()

    .. py:attribute:: cursor
    

    .. py:attribute:: diag

        Диагностический объект ошибки :py:class:`psycopg2.extensions.Diagnostics()`


    .. py:attribute:: pgcode

        .. code-block:: py

            err.pgcode
            # '42P01'


    .. py:attribute:: pgerror

        .. code-block:: py

            err.pgerror
            """
            ERROR:  relation "barf" does not exist
            LINE 1: SELECT * FROM barf
            """


IntegrityError()
----------------

.. py:class:: IntegrityError()


InterfaceError()
----------------

.. py:class:: InterfaceError()


InternalError()
---------------

.. py:class:: InternalError()


NotSupportedError()
-------------------

.. py:class:: NotSupportedError()


OperationalError()
------------------

.. py:class:: OperationalError()


ProgrammingError()
------------------

.. py:class:: ProgrammingError()


Warning()
---------

.. py:class:: Warning()