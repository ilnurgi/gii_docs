.. py:module:: django.apps

django.apps
===========

.. code-block:: py

    # __init__.py

    default_app_config = 'app_name.apps.BlogConfig'

    # apps.py

    from django.apps import AppConfig

    class BlogConfig(AppConfig):
        
        name = 'blog'
        verbose_name = 'blog'

AppConfig
---------

.. py:class:: AppConfig()

    Конфигуратор приложения

    .. py:attribute:: name
    
    .. py:attribute:: verbose_name

        эта строка будет отображаться в админке