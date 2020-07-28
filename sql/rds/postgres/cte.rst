.. title:: postgres cte

.. meta::
    :description:
        Справочная информация по субд postgres, cte
    :keywords:
        postgres cte

cte
===

.. code-block:: sql

    with

      cte_name(column_list)
    as 
    (
        query
    )

    statement

.. code-block:: sql

    with recursive

      cte_name(column_list)
    as 
    (
        query
        union
        select * from cte_name
    )

    statement
