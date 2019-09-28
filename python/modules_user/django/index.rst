Django
======

Структура django приложения

    * application - папка приложения

        * :ref:`django_management` - консольные утилиты

            * commands - папка со скриптами

                * _private.py - приватная команда

                * command_name.py - команда

        * __init__.py - приложение - пакет

            .. code-block:: py

                # __init__.py

                # конфигуратор приложения
                default_app_config = 'app_name.apps.AppConfig'



        * admin.py - настройка админки

        * apps.py - настройка приложения, :py:mod:`django.apps`

        * feeds.py - rss рассылка

        * forms.py - формы приложения

        * models.py - модели приложения

        * signals.py - сигналы

        * sitemaps.py - карта сайта

        * tests.py - тесты приложения

        * urls.py - маршруты, роутинг урлов

        * views.py - представления

        * migrations - пакет с миграциями приложения

            * __init__.py - пакет

        * templates - папка с шаблонами

            * index.html - какой то шаблон

        * templatetags - папка с самописными тегами для шаблонов

            * tag.py - какой то тег

        * static - папка со статикой

            * app.css - какая то статика


.. toctree::
    :maxdepth: 1

    apps
    settings
    models/index
    views/index
    forms/index
    templates
    urls
    signals
    contrib/index
    cli
    management/index
    faq
