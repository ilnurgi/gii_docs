.. _nginx_server:

server
======

.. code-block:: nginx

    http {
        server {
            listen 80;
            server_name ilnurgi.ru;
        }
    }


listen
------

Порт для прослушки

.. code-block:: nginx

    listen 80;


root
----

Корневая папка для сервера

.. code-block:: nginx

    root /var/www/ilnurgi/build/


server_name
-----------

Имя сервера, домен или поддомен

.. code-block:: nginx

    server_name ilnurgi.ru;
    server_name 192.168.0.1;




