.. _nginx_server:

server
======

.. code-block:: js

    http {
        server {
            listen 80;
            server_name ilnurgi.ru;
        }
    }


listen
------

Порт для прослушки

.. code-block:: js

    listen 80;


root
----

Корневая папка для сервера

.. code-block:: js

    root /var/www/ilnurgi/build/


server_name
-----------

Имя сервера, домен или поддомен

.. code-block:: js

    server_name ilnurgi.ru;
    server_name 192.168.0.1;




