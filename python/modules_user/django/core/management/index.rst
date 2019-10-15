.. title:: python django core management

.. meta::
    :description: 
        Справочная информация по консольным утилитам библиотеке django, 
        написанный на языке программирования python,
        для разработки веб приложений.        
    :keywords: python, django, python django, python django management

.. py:module:: django.core.management

management
==========

Консольные утилиты

.. toctree::
    :maxdepth: 1

    migrations


createsuperuser
---------------

.. code-block:: sh

    # создать суперпользователя
    $ python manage.py createsuperuser

dumpdata
--------

.. code-block:: sh

    # выгружаем данные для конкретного приложения
    $ python manage.py dumpdata app_name --indent=2


loaddata
--------

.. code-block:: sh

    # загружаем данны для конкретного приложения
    $ python manage.py loaddata data.json


runserver
---------

.. code-block:: sh

    # запускает сервер разработки
    $ python manage.py runserver


startapp
--------

.. code-block:: sh

    # создает приложение в проекте
    $ python manage.py startapp my_app