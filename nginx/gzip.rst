.. title:: nginx gzip

.. meta::
    :description:
        Справочная информация по nginx gzip.
    :keywords:
        nginx gzip

gzip
====

gzip
----

Включение/выключение gzip сжатия

.. code-block:: nginx

    http {
        gzip on;

        server {
            location / {
                gzip off;
            }
        }
    }


gzip_comp_level
---------------

Уровень сжатия от 1 до 9.

.. code-block:: nginx

    gzip_comp_level 3;


gzip_disable
------------

Выключает сжатие для указанного юзер агента

.. code-block:: nginx

    gzip_disable "msie6";


gzip_min_length
---------------

Минимальный размер для сжатия, все что меньше, пропускаем

.. code-block:: nginx

    gzip_min_length 100;


gzip_proxied
------------

Проксировать запросы на прокси сервера

.. code-block:: nginx

    gzip_proxied any;


gzip_static
-----------

Отдает только статичные файлы, заранее сжатые в формате gzip.
.. code-block:: nginx

    gzip_static on;


gzip_types
----------

Типы файлов, которые необходимо сжимать

.. code-block:: nginx

    gzip_types text/plain text/css;
    gzip_types text/javascript;


gzip_vary
---------

Добавляет заголовок Vary: Accept-Encoding

.. code-block:: nginx

    gzip_vary on;
