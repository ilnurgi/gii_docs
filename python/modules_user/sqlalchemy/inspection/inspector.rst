.. title:: python sqlalchemy inspector

.. meta::
    :description:
        Справочная информация по python модулю sqlalchemy.inspect.
    :keywords:
        python sqlalchemy inspector

.. py:currentmodule:: sqlalchemy.inspect

Inspector()
===========

.. py:class:: Inspector()

    .. code-block:: py

        inspector = inspect(engine)


    .. py:method:: get_columns()

        Возвращает сведения по столбцам таблицы

        .. code-block:: py

            inspector.get_columns('user')
            # [{...}]


    .. py:method:: get_foreign_keys()

        .. code-block:: py

            inspector.get_foreign_keys('user')
            # [{...}]


    .. py:method:: get_table_names()

        Возвращает список названий таблиц базы

        .. code-block:: py

            inspector.get_table_names()
            # ['adress', 'users']