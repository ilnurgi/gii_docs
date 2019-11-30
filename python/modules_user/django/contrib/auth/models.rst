.. title:: python django contrib auth models

.. meta::
    :description: 
        Справочная информация по настройкам прав пользователей библиотеки django, 
        написанный на языке программирования python,
        для разработки веб приложений.        
    :keywords: 
        python, 
        django, 
        python django contrib auth models, 
        python django auth models,
        django contrib auth models, 
        django auth models

.. py:module:: django.contrib.auth.models

models
======

User
----

.. py:class:: django.contrib.auth.models.User

    Пользователь

    .. py:attribute:: email

        Строка, электронная почта

    .. py:attribute:: is_active

        Булево, активный пользователь

    .. py:attribute:: is_staff

        Булево, персонал сайта, имеет возможность войти в админку

    .. py:attribute:: is_superuser

        Булево, суперпользователь


    .. py:attribute:: objects

        :py:class:`django.contrib.auth.models.UserManager`

        Менеджер модели


    .. py:method:: get_full_name()

        Возвращает строку, фамилию и имя пользователя

    .. py:method:: get_short_name()

        Возвращает строку, фамилию пользователя

    .. py:method:: get_username()

        Возвращает строку, логин пользователя


    .. py:method:: has_perm(permission)

        Возвращает булево, имеет ли пользователь указанное право

        .. code-block:: py

            simple_user.has_perm('good.add_good')
            # False

            super_user.has_perm('good.add_good')
            # True

            super_user.has_perm('does.not.exists')
            # True
            # суперпользователь имеет право на все


    .. py:method:: has_perms(perms_list)

        Возвращает булево, имеет ли пользователь указанные права

        .. code-block:: py

            user.has_perms(['good.add_good', 'good.delete_good'])
            # True


    .. py:method:: is_anonymous()

        Возвращает булево, гость

    .. py:method:: is_authenticated()

        Возвращает булево, авторизован ли пользователь.


UserManager
-----------

.. py:class:: UserManager()

    Менеджер User модели

    .. code-block:: py

        User.objects


    .. py:method:: create_superuser(username, email, password)

        Создает супер пользователя в базе данных и возврщает :py:class:`django.contrib.auth.models.User`.

        .. code-block:: py

            super_user = User.objects.create_superuser(
                username='ilnurgi',
                email='email',
                password='password'
            )


    .. py:method:: create_user(username)

        Создает пользователя в базе данных и возврщает :py:class:`django.contrib.auth.models.User`.

        .. code-block:: py

            user = User.objects.create_user(username='ilnurgi')
