.. title:: python django urls

.. meta::
    :description: 
        Справочная информация по роутингу библиотеки django, 
        написанный на языке программирования python,
        для разработки веб приложений.        
    :keywords: 
        python, 
        django, 
        python django urls,
        django urls

.. py:module:: django.urls

urls
====

Роутинг

.. code-block:: py

    # urls.py

    from django.conf import settings
    from django.urls import patterns, include, url, static
    from django.contrib import admin
    from django.contrib.admin.decorators import (
        login_required, permission_required)

    from application import views

    urlpatterns = patterns('',
        url(
            r'^admin/',
            url(admin.site.urls),
        ),
        url(
            r'^application/',
            url("application.urls"),
        ),
        url(
            r'^application/index',
            views.index,
            name="index",
        ),
        url(
            r'^good/(?P<good_id>\d+)',
            views.good,
            name="good",
        ),
        url(
            r'^good/(?P<good_id>\d+)',
            views.IndexView.as_view(),
            name="good",
        ),
        url(
            r'^good/(?P<good_id>\d+)',
            login_required(views.IndexView.as_view()),
            name="good",
        ),
        url(
            r'^good/(?P<good_id>\d+)',
            permission_required("good.add_good")(views.IndexView.as_view()),
            name="good",
        ),
        url(
            r'^good/',
            include(
                'blog.urls',
                namespace="blog",
                app_name="blog",
            ),
        ),
    )

    if settings.DEBUG:
        
        # раздаем медиа файлы в режиме дебага
        urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

        # раздаем статику в режиме дебага
        urlpatterns.extend(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))


.. code-block:: py

    # urls.py

    from django.conf import settings
    from django.contrib import admin
    from django.contrib.admin.decorators import (
        login_required, permission_required)
    from django.urls import path

    from application import views

    urlpatterns = [
        path('search/', views.SearchView.as_view(), name='search_result'),
        path('', views.HomeView.as_view(), name='home'),
    ]