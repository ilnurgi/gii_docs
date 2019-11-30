.. title:: python django contrib site

.. meta::
    :description: 
        Справочная информация по админке библиотеки django, модуль site,
        написанный на языке программирования python,
        для разработки веб приложений.        
    :keywords: 
        python, 
        django, 
        python django, 
        python django contrib admin site, 
        python django contrib site, 
        django contrib admin site, 
        django contrib site

.. py:module:: django.contrib.admin.site

site
====

register
--------

.. py:method:: register(*models)

    Регистрирует модель в админке

    .. code-block:: py

        from django.admin.site import register

        from some_app.models import SomeModel

        register(SomeModel)
        