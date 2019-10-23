.. title:: javascript parcel

.. meta::
    :description:
        Описание javascript библиотеки parcel.
    :keywords:
        javascript parcel

parcel
======

.. code-block:: sh

    $ npm install parcel-bundler

    # запуск сервера разработки
    $ parcel index.html
    Server running at http://localhost:1234

    # сборка проекта
    $ parcel build index.js


.. code-block:: html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">

        <!-- parcel автоматический работает с scss файлами -->
        <link rel="stylesheet" href="style.scss">
        <title>Parcel Tutorial</title>
    </head>
    <body>
        <script src="index.js"></script>
    </body>
    </html>


