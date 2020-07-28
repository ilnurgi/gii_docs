.. title:: sql agregate functions

.. meta::
    :description: 
        Справочная информация по sql, агрегатные функции.
    :keywords: 
        sql agregate functions

Агрегатные функции
==================


AVG
---

.. py:method:: AVG()  

    Среднее значение в указанном поле

    .. code-block:: sql

        select
          sex
          , avg(age) age_avg
        from
          table
        group by
          sex
        order by
          age_avg desc

    .. code-block:: sql

        select
          user_id
          , avg(rating) avg_rating
        from
          ratings
        group by
          user_id
        having 
          avg(rating) < 4.5


COUNT
-----

.. py:method:: COUNT()
    
    Количество записей в указанном поле

    .. code-block:: sql

        SELECT 
          COUNT(*)
          , COUNT(distinct id)
        from 
          table


.. py:method:: MAX(<поле>)  

    максимальное значение в указанном поле

    .. code-block:: c

        SELECT MAX(age) from table


.. py:method:: MIN(<поле>)
    
    минимальное значение в указанном поле

    .. code-block:: c

        SELECT MIN(age) from table


SUM
---

.. py:method:: SUM()

    Сумма значение в указанном поле

    .. code-block:: sql

        SELECT 
          SUM(age) 
        from 
          table

