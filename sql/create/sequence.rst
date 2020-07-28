.. title:: sql create sequence

.. meta::
    :description:
        Справочная информация по sql, create sequence.
    :keywords:
        sql create sequence

CREATE SEQUENCE
===============

.. code-block:: sql

    create sequence my_table_id_seq;

    create table ny_table(
        id integer
            not null
            default nextval('my_table_id_seq')
    );

    alter sequence my_table_id_seq owned by my_table.id;

.. code-block:: sql

    create sequence seq
        increment by 10
        start 100;
