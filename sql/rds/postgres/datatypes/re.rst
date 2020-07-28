.. title:: postgres re

.. meta::
    :description: 
        Справочная информация по posqtgres, регулярные выражения.
    :keywords: 
        postgres re

re
==

regexp_split_to_array()
-----------------------

.. code-block:: psql

    select 
      prt[1] person_id
      , prt[2] person_name
    from ( 
      select 
        regexp_split_to_array(str, ',') prt
      from (
        values
          ('1, ilnurgi1')
          , ('2, ilnurgi2') 
      ) t(str)
    ) t
    
    /*
    person_id | person_name
    ----------+------------
    1         | ilnurgi1
    2         | ilnurgi2
    */


regexp_split_to_table()
-----------------------

.. code-block:: psql

    select 
      regexp_split_to_table(
        $$
        1;ilnurgi1
        2;ilnurgi2
        $$
        , E'\\n'
      ) ptr

    /*
    ptr
    -----------
    1; ilnurgi1
    2; ilnurgi2
    */
