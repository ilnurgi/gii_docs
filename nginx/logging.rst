logging
=======

.. code-block:: nginx

    http {
        acces_log off;
    }

access_log
----------

.. code-block:: nginx

    access_log off;


error_log
---------

Используется в контекстах: main, :ref:`nginx_http`, :ref:`nginx_server`, :ref:`nginx_location`.

.. code-block:: nginx

    error_log file|stderr [debug|info|notice|warn|error|alert|emerg];

    error_log off;
    error_log /var/log/nginx/error_ilnurgi.log;
    error_log /var/log/nginx/error_ilnurgi.log debug;