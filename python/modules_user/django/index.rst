.. title:: python django

.. meta::
    :description: 
        Справочная информация по python библиотеке django.        
    :keywords:
        python django

.. py:module:: django

django
======

.. code-block:: sh

    # устанавливаем библиотеку
    pip install django

    # стартуем проект
    django-admin startproject project_name


Структура django приложения

    * application - папка приложения

        * management - папка консольных команд, :py:mod:`django.core.management`

            * commands - папка со скриптами

                * _private.py - приватная команда

                * command_name.py - команда

        * __init__.py - приложение - пакет

            .. code-block:: py

                # __init__.py

                # конфигуратор приложения
                default_app_config = 'app_name.apps.AppConfig'

        * admin.py - настройка админки, :py:mod:`django.contrib.admin`

        * apps.py - настройка приложения, :py:mod:`django.apps`

        * feeds.py - rss рассылка

        * forms.py - формы приложения

        * models.py - модели приложения, :py:mod:`django.db.models`

        * signals.py - сигналы

        * sitemaps.py - карта сайта

        * tests.py - тесты приложения

        * urls.py - маршруты, роутинг урлов, ;py:mod:`django.urls`

        * views.py - представления, :py:mod:`django.views`

        * migrations - пакет с миграциями приложения

            * __init__.py - пакет

        * templates - папка с шаблонами

            * index.html - какой то шаблон

        * templatetags - папка с самописными тегами для шаблонов

            * tag.py - какой то тег

        * static - папка со статикой

            * app.css - какая то статик


.. toctree::
    :maxdepth: 1

    apps
    settings
    forms/index
    templates
    urls
    signals
    cli
    faq

.. toctree::
    :maxdepth: 2

    contrib/index
    core/index
    db/index
    views/index