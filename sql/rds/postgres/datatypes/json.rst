.. title:: postgres json

.. meta::
    :description: postgres json
    :keywords: postgres json

json
====

.. code-block:: psql

  select
    info ->> 'customer' customer
    , info -> 'items' ->> 'product' product
  from
    orders


json_object
-----------

Возвращает json объект

.. code-block:: psql

    select
      json_object(
        array_agg("id")::text[]
        , array_agg("name")::text[]
      )
    from
      "cities"

    /*
      {
        "1": "Moscow",
        "2": "Kazan"
      }
    */