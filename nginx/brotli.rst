.. title:: nginx brotli

.. meta::
    :description:
        Справочная информация по nginx brotli.
    :keywords:
        nginx brotli

brotli
======

brotli
------

Включает/выключает сжатие brotli

.. code-block:: nginx

    brotli on;


brotli_comp_level
-----------------

Степень сжатия от 1 до 11

.. code-block:: nginx

    brotli_comp_level 5;


brotli_static
-------------

.. code-block:: nginx

    brotli_static on;


brotli_types
------------

Типы сжимаемых данных

.. code-block:: nginx

    brotli_types text/plain;
