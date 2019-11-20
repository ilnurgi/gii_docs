.. title:: python sqlalchemy engine

.. meta::
    :description:
        Справочная информация по python модулю sqlalchemy.engine.ResultProxy.
    :keywords:
        python sqlalchemy resultproxy

.. py:currentmodule:: sqlalchemy.engine

ResultProxy
===========

.. py:class:: ResultProxy()

    Результат выполнения запроса в базу.

    .. code-block:: py

        result = engine.execute(sql)


    .. py:method:: close()

        Ручное закрытие соединения

        .. code-block:: py

            result.close()


    .. py:method:: fetchall()

        Возвращает все записи из результата.

        .. code-block:: py

            rows = result.fetchall()


    .. py:method:: fetchone()

        Возвращает одну запись из результата.

        .. code-block:: py

            row = result.fetchone()
