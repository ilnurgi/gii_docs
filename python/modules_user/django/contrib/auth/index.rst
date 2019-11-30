.. title:: python django contrib auth

.. meta::
    :description: 
        Справочная информация по настройкам прав пользователей библиотеки django, 
        написанный на языке программирования python,
        для разработки веб приложений.        
    :keywords: 
        python, 
        django, 
        python django contrib auth, 
        python django auth,
        django contrib auth, 
        django auth

.. py:module:: django.contrib.auth

auth
====

.. toctree::
    :maxdepth: 1

    decorators
    models
    views

Пользователи, права, авторизация.

Права задаются в виде app_name.action_model.

Есть несколько видов действий:

    * add - добавление

    * change - изменение

    * delete - удаление

    * view - просмотр

но можно создать и свои :ref:`models_meta_permissions`.


По умолчанию, в контекст шаблонов добавляются переменные user и perms.

* user - пользователь

    .. code-block:: htmldjango

        {% if user.is_authenticated %}            
        {% endif %}

* perms - права, которыми обладает пользователь

    .. code-block:: htmldjango

        {% if perms.good.add_good %}            
        {% endif %}


Конфигурирование
----------------

* :ref:`settings_login_redirect_url`
* :ref:`settings_login_url`
* :ref:`settings_logout_url`


authenticate
------------

.. py:method:: authenticate(username, password)

    Аутентификация пользователя, если пользователя нет вернет None.

    .. code-block:: py

        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
        )


login
-----

.. py:method:: login(request, user)

    Авторизация пользователя

    .. code-block:: py

        login(request, user)