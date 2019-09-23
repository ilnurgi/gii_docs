.. _django_management:

management
==========

Консольные утилиты

.. toctree::
    :maxdepth: 1

    migrations


dumpdata
--------

Выгрузка данных

.. code-block:: sh

    // выгружаем данные для конкретного приложения
    python manage.py dumpdata app_name --indent=2


loaddata
--------

.. code-block:: sh

    // загружаем данны для конкретного приложения
    python manage.py loaddata data.json
