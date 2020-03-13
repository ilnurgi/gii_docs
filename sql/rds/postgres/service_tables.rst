.. title:: postgres service tables

.. meta::
    :description:
        Справочная информация по субд postgres, описание сервисных таблиц
    :keywords:
        postgres service tables

Сервисные таблицы
=================

information_schema
------------------

Список таблиц

.. code-block:: sql

    select
        table_name
    from
        information_schema.tables
    where
        table_schema = 'public'
    order by table_name;

.. code-block:: text

    table_name
    ----------
    sessions
    books
    authors
