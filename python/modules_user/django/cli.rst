.. title:: python django cli

.. meta::
    :description: 
        Справочная информация по python библиотеке django, консольные команды.
    :keywords:
        python django cli

.. py:currentmodule:: django

Консольные команды
==================


.. _cli_compilemessages:

compilemessages
---------------

Скомпилировать файлы локализации

.. code-block:: sh

    python manage.py compilemessages

* :ref:`cli_makemessages`


.. _cli_createsuperuser:

createsuperuser
---------------

Создать суперпользователя

.. code-block:: sh

    python manage.py createsuperuser


.. _cli_makemessages:

makemessages
------------

Создать файлы локализации

.. code-block:: sh

    python manage.py makemessages

:ref:`cli_compilemessages`


.. _cli_makemigrations:

makemigrations
--------------

Создать файлы миграции

* name - название миграции

.. code-block:: sh

    python manage.py makemigrations app_name

    python manage.py makemigrations shop --name "add_translation_model"

    # datamigration
    python manage.py makemigrations shop --empty

* :ref:`cli_migrate`
* :ref:`cli_sqlmigrate`


.. _cli_migrate:

migrate
-------

Миграция базы данных

.. code-block:: sh

    python manage.py migrate

* :ref:`cli_makemigrations`
* :ref:`cli_sqlmigrate`


.. _cli_runserver:

runserver
---------

Запуск сервера разработки, по умолчанию на 127.0.0.1:8000

* settings - моудль файла настроек

.. code-block:: sh

    python manage.py runserver

    python manage.py runserver 0.0.0.0:80

    python manage.py runserver --settings mysite.settings


.. _cli_shell:

shell
-----

Запустить проект в терминале, в python

.. code-block:: sh

    python manage.py shell


.. _cli_sqlmigrate:

sqlmigrate
----------

Выводит sql запросы миграции

.. code-block:: sh

    python manage.py sqlmigrate app_name 0001
    """
    BEGIN;
    CREATE TABLE "blog_post" (
        "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        "title" varchar(250) NOT NULL,
        "slug" varchar(250) NOT NULL,
        "body" text NOT NULL,
        "publish" datetime NOT NULL,
        "created" datetime NOT NULL,
        "updated" datetime NOT NULL,
        "status" varchar(10) NOT NULL,
        "author_id" integer NOT NULL REFERENCES "auth_user" ("id"));
    CREATE INDEX "blog_post_2dbcba41" ON "blog_post" ("slug");
    CREATE INDEX "blog_post_4f331e2f" ON "blog_post" ("author_id");
    COMMIT;
    """

* :ref:`cli_makemigrations`
* :ref:`cli_migrate`


.. _cli_startapp:

startapp
--------

Создать приложение в проекте

.. code-block:: sh

    django-admin startapp blog

* :ref:`cli_startproject`

.. _cli_startproject:

startproject
------------

Создать проект, генерирует структуру.

.. code-block:: sh

    django-admin startproject mysite

* :ref:`cli_startapp`


.. _cli_test:

test
----

Прогнать тесты проекта

.. code-block:: sh

    python manage.py test

    # детализированный вывод информации, 0..2
    python manage.py test --verbosity=2
