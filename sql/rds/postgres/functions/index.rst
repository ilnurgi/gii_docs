.. title:: postgres functions

.. meta::
    :description: 
        Справочная информация по функциям postgres
    :keywords: 
        postgres functions

Встроенные функции
==================

.. toctree::
    :maxdepth: 2

    window
    
generate_series()
-----------------

.. py:function:: generate_series()

    .. code-block:: sql

        select 
            *
        from
            generate_series(1, 10) as f(x);

    .. code-block:: text

        x
        ---
          1
        ...
         10

nextval()
---------

Извлекает следующее значение из sequence