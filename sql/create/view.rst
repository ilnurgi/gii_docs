.. title:: sql create view

.. meta::
    :description:
        Справочная информация по sql, create view.
    :keywords:
        sql create view

CREATE VIEW
===========

.. code-block:: sql

    CREATE VIEW view_name AS query;

    select * from view_name;

.. code-block:: sql

    CREATE OR REPLACE view_name as query;

.. code-block:: text

    CREATE MATERIALIZED VIEW view_name AS query WITH [NO] DATA;

    REFRESH MATERIALIZED VIEW view_name;


* **WITH DATA** - загрузить данные сразу
* **WITH NO DATA** - позже
