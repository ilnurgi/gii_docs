nginx
=====

`wiki.nginx.org <http://wiki.nginx.org/>`_

.. code-block:: sh

    # перечитать конфигурационный файл
    service nginx reload

    # протестировать конфигурационный файл на валидность
    service nginx -t


.. toctree::
    :maxdepth: 1

    events
    http
    location
    logging
    server
    types

.. code-block:: js

    worker_process 1;
    # worker_process auto;

    events {}
    
    access_log off;

    http {

        set $no_cache 0;

        if ($request_method = POST){
            set $no_cache 1;
        }

        if ($query_string != ""){
            set $no_cache 1;
        }

        if ($request_uri ~* "/wp-admin"){
            set $no_cache 1;
        }
    }


gzip
----

.. code-block:: js

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

Уровень сжатия, как вариант использовать от 2 до 4.

.. code-block:: js

    gzip_comp_level 3;


gzip_disable
------------

Выключает сжатие для указанного юзер агента

.. code-block:: js

    gzip_disable "msie6";


gzip_min_length
---------------

Минимальный размер для сжатия, все что меньше, пропускаем

.. code-block:: js

    http {
        gzip on;

        # минимальный размер для сжатия
        gzip_min_length 100;
    }

gzip_types
----------

Типы файлов, которые необходимо сжимать

.. code-block:: js

    gzip_types text/plain text/css;
    gzip_types text/javascript;


limit_con_zone
--------------

Лимит относительно чего 

.. code-block:: js

    http {
        # ограничение паралельных соединений в блоке сервера, 5 мегабайт
        limit_con_zone $server_name zone=per_vhost:5m;

        # количество паралельных запросов относительно ip адреса
        limit_con_zone $binary_remote_addr zone=per_ip:5m;
    }

limit_req_zone
--------------

.. code-block:: js

    http {
        limit_req_zone $binary_remote_addr zone=one_per_sec:5m rate=1r/s;

        server {
            location {
                limit_req zone=one_per_sec burst=5;
            }
        }
    }
