.. title:: linux curl

.. meta::
    :description:
        Справочная информация по встроенной в linux утилите curl.
    :keywords:
        linux curl

curl
====

.. code-block:: sh

    $ curl http://localhost:8000/posts \
        -x POST \
        -H "Content-Type: application/json" \
        -d '{"title": "Post 1"}'
    {
        "title": "Post 1"
    }
