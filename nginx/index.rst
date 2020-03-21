.. title:: nginx

.. meta::
    :description:
        Справочная информация по nginx.
    :keywords:
        nginx

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

    brotli
    events
    gzip
    http
    location
    logging
    server
    types

.. code-block:: nginx

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


limit_con_zone
--------------

Лимит относительно чего

.. code-block:: nginx

    http {
        # ограничение паралельных соединений в блоке сервера, 5 мегабайт
        limit_con_zone $server_name zone=per_vhost:5m;

        # количество паралельных запросов относительно ip адреса
        limit_con_zone $binary_remote_addr zone=per_ip:5m;
    }

limit_req_zone
--------------

.. code-block:: nginx

    http {
        limit_req_zone $binary_remote_addr zone=one_per_sec:5m rate=1r/s;

        server {
            location {
                limit_req zone=one_per_sec burst=5;
            }
        }
    }
