types
=====

Задает соответсвие mime типов

.. code-block:: js

    http {
        types {
            text/html text;
            text/css css;

        }
    }

.. code-block:: js

    http {
        include mime.types;
    }