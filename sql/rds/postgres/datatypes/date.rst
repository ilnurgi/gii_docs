.. title:: postgres date

.. meta::
    :description: 
        Справочная информация по posqtgres, тип данных date.
    :keywords: 
        postgres date

date
====

to_date()
---------

Возвращает дату из строки

.. code-block:: psql

    select
      to_date(date_str, 'DD.MM.YYYY') dt
    from
      table_name
