.. title:: python django contrib auth decorators

.. meta::
    :description: 
        Справочная информация по настройкам прав пользователей библиотеки django, 
        написанный на языке программирования python,
        для разработки веб приложений.        
    :keywords: 
        python, 
        django, 
        python django contrib auth decorators, 
        python django auth decorators,
        django contrib auth decorators, 
        django auth decorators

.. py:module:: django.contrib.auth.decorators

decorators
==========


login_required
--------------

.. py:method:: django.contrib.auth.decorators.login_required

    Декоратор проверки авторизации пользователя

    Если пользователь не авторизован, то он будет перенаправлен на
    :ref:`settings_login_url`

    .. code-block:: py

        from django.contrib.auth.decorators import login_required

        @login_required
        def index(request):
            return render(request, 'index.html')


permission_required()
---------------------

.. py:method:: permission_required(permission)

    Декоратор проверки авторизации пользователя и наличия прав

    .. code-block:: py

        from django.contrib.auth.decorators import permission_required

        @permission_required('app_name.action_model')
        def index(request):
            return render(request, 'index.html')
            