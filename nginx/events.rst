events
======

.. code-block:: js

    events {
        worker_connections 1024;
        multi_accept on;
        use epoll;
    }