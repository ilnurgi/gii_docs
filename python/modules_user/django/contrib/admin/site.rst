.. py:module:: django.admin.site

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
        