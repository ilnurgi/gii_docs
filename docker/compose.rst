.. title:: docler-compose

.. meta::
    :description lang=ru: Описание docker compose
    :description lang=en: docker compose notes
    :keywords lang=ru: docker compose
    :keywords lang=en: docker compose

docker-compose
==============

.. code-block:: py

    docker
    - nginx
    - - conf.d
    - - - default.conf
    - - dockerfile
    - - nginx.conf
    - php
    - - dockerfile
    docker-compose.yaml
    index.html

.. code-block:: yaml

    version: '3'
    services: 
        nginx:
            build: ./docker/nginx
            ports:
                - "8080:80"
            volumes:
                - ./:/app
                - ./docker/nginx/nginx.conf:/etc/nginx/nginx/conf
                - ./docker/nginx/conf.d:/etc/nginx/conf.d
            depends_on:
                - php 
        php:
            build: ./docker/php
            volumes:
                - ./:/app

up
--

* --build - пересобрать контейнеры
* -d - detach - запустить контейнеры в фоне

.. code-block:: sh

    docker-compose up --build -d