.. title:: Конспекты по docker

.. meta::
    :description lang=ru: конспекты по docker, описание консольных команд
    :description lang=en: docker cli command notes
    :keywords lang=ru: docker
    :keywords lang=en: docker

Docker
======

.. toctree::
    :maxdepth: 1

    dockerfile
    compose


docker
------

Выводит в косноль список всех достпных команд

.. code-block:: sh

    $ docker
    ...
    run Run a comand in a new container
    ...


build
-----

Собрать образ из dockerfile

* -t - имя образа

.. code-block:: sh

    $ docker build ./

    $ docker build ./ -t "name:tag"


exec
----

Выполнить команду в контейнере

* -it - интерактивный режим

.. code-block:: sh

    $ docker ps
    ...
    123123123   nginx   ....
    ...

    $ docker exec -it 123123123 bash
    root@123123123:/#


images
------

Выводит в консоль список локальных образов

.. code-block:: sh

    $ docker images
    REPOSITORY  TAG     IMAGE ID    CREATED         SIZE
    ...
    nginx       latest  ...         5 months ago    312MB
    postgres    11.1    ...         5 months ago    312MB
    ...

kill
----

Принудительное завершение контейнер

.. code-block:: sh

    $ docker ps
    ...
    123123123   php:7.1-cli ....
    ...

    $ docker kill 123123123
    123123123


logs
----

Вывод логов контейнера

* -f - аналог tail -f

.. code-block:: sh

    $ docker ps
    ...
    123123123   nginx ....
    ...

    $ docker logs 123123123
    127.......

    $ docker logs -f 123123123
    127...
    127...


pause/unpause
-------------

Поставить контейнер на паузу или вывести из состояния паузы

.. code-block:: sh

    $ docker ps
    ...
    123123123   php:7.1-cli ....
    ...

    $ docker pause 123123123
    123123123

    $ docker unpause 123123123
    123123123


ps
--

Вывести в консоль список запущенных контейнеров

* -a - покажет историю запуска контейнеров

.. code-block:: sh

    $ docker ps
    CONTAINER ID    IMAGE   COMMAND     CREATED     STATUS          PORTS                   NAMES
    asdasdaskjd     nginx   "nginx -g"  12 sec ago  Up 11 seconds   0.0.0.0:8080->80/tcp    blablabla


pull
----

Скачивает образ из официального хранилища

.. code-block:: sh

    $ docker pull nginx

.. code-block:: sh

    # качаем образ my/nginx из хранилища mereg:port
    $ docker pull myreg:port/my/nginx


rm/rmi
------

Удаляет локальный образ

.. code-block:: sh

    docker rmi nginx:latest


run
---

Скачивает образ в реестр, устанавливает и запускает контейнер

* -d - detach - запустить контейнер в фоне
* -e - переменные окружения
* --env-file - файл переменных окружения
* -it - запустить контейнер в интерактивном режиме
* -p - проброс портов, по умолчанию на все сетевые интерфейсы
* -v - проброс папок

.. code-block:: sh

    # скачать образ nginx
    # запустить контейнер nginx
    # зпустить bash внутри контейнера
    $ docker run -it nginx bash
    root@:/#

.. code-block:: sh

    # скачать и запустить контейнер
    # выполнить команду внутри контейнера
    $ docker run nginx cat /etc/nginx/nginx.conf

.. code-block:: sh

    # пробросить внутрений порт контейнера 8080 на 80 порт хоста
    $ docker run -p 8080:80 nginx

    # -d, запустить в фоне
    $ docker run -p 8080:80 -d nginx
    asdasdaskjdasjdasd

    $ docker run -p 8080:80  -p 443:443 -d nginx

    $ docker run -v ~/project:/app nginx

    $ docker run -e "HOME=/app" nginx

    $ docker run --env-file=.env nginx

.. code-block:: sh

    $ docker images
    ...
    123123123   php:7.1-cli ....
    ...

    $ docker run -it 123123123
    root@123123123:/#

.. code-block:: sh

    $ docker run -it php:7.1-cli
    php > echo 2+2;
    4


start/stop
----------

Запустить или остановить контейнер

.. code-block:: sh

    .. code-block:: sh

    $ docker ps
    ...
    123123123   php:7.1-cli ....
    ...

    $ docker stop 123123123
    123123123

    $ docker start 123123123
    123123123


stats
-----

Информация о потреблении ресурсов

.. code-block:: sh

    $ docker stats
    CONTAINER ID    NAME    CPU %   MEM USAGE / LIMIT       ...
    123123          nginx   0.00%   1.436MiB / 7.644 GiB    ...
