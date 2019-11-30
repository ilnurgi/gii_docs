.. title:: dockerfile

.. meta::
    :description lang=ru: описание dockerfile
    :description lang=en: dockerfile description
    :keywords lang=ru: dockerfile
    :keywords lang=en: dockerfile

dokerfile
=========

.. code-block:: text

    FROM php:7.3-cli
    MAINTAINER ilnurgi

    RUN apt update && apt install -y mc
    
    COPY . /app
    WORKDIR /app
    CMD ["php-fpm"]


CMD
---

Команда запуска

.. code-block:: text

    CMD ["php-fpm"]


COPY
----

Директива позволяет скопировать данные из папки хоста в папку образа

.. code-block:: text

    COPY . /app


FROM
----

Директива указывает образ, на основе которого собран текущий образ

.. code-block:: text

    FROM php:7.3-cli


MAINTAINER
----------

Директива указывает автора образа

.. code-block:: text

    MAINTAINER ilnurgi


RUN
---

Директива указывает какие команды запустить в контейнере

.. code-block:: text

    RUN app update && apt install -y mc


WORKDIR
-------

Директива указывает рабочую директорую в образе

.. code-block:: text

    WORKDIR /app
