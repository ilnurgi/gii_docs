.. title:: sql functions

.. meta::
    :description:
        Справочная информация по sql, functions
    :keywords:
        sql functions

Функции
=======

any()
-----

.. code-block:: sql

    select 
      * 
    from (
        values
          (1, 'ilnurgi1')
          , (2, 'ilnurgi2')
      ) t(p_id, p_name)
    where 
      p_id = any('{1,3}'::int[]);

    /*
    p_id | p_name
    -----+-------
    1    | ilnurgi1
    */


unnest()
--------

Разворачивает массив

.. code-block:: sql

    select
      *
    from 
      unnest('{1,2,3}::int[]')

    /*
    unnest
    ------
    1
    2
    3
    */