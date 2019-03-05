.. _nginx_location:

location
========

.. code-block:: json

    http {
        server {

            # совпадение префикса
            location / {
                return 200 'Hello world';
            }

            # полное совпадение
            location = / {

            }

            # регулярка nginx
            location ~ /ilnurgi[0-9] {

            }

            # регулярка nginx, без проверки регистра
            location *~ /ilnurgi[0-9] {

            }

            # префикс преимущества
            location ^~ / {

            }

            # кешируем статику на клиенте
            location ~* \.(css|js|png) {
                # доступ кешировать не надо
                access_log off;
                # клиентский кеш на 1 месяц
                expires 1M;
            }

        }
    }

expires
-------

Время кеша ресурса в браузере

.. code-block:: js
    
    # 1 месяц
    expires 1M;

    # 1 день
    expires 1d;


rewrite
-------

.. code-block:: js

    rewrite ^ /index.html;


root
----

.. code-block::js

    root /var/ww/ilnurgi/;


try_files 
---------

.. code-block:: js

    try_files $uri =404;