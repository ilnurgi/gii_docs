.. title:: python sqlalchemy transaction

.. meta::
    :description:
        Справочная информация по python модулю sqlalchemy.engine.Transaction.
    :keywords:
        python sqlalchemy transaction

.. py:currentmodule:: sqlalchemy.engine

Transaction
===========

.. py:class:: Transaction()

    Объект транзакции

    .. code-block:: py

        trans = conn.begin()


    .. py:method:: close()

        Закрывает транзакцию

        .. code-block:: py

            trans.close()


    .. py:method:: commit()

        Фиксирует изменения

        .. code-block:: py

            trans.commit()


    .. py:method:: rollback()

        Отменяет изменения

        .. code-block:: py

            trans.rollback()
