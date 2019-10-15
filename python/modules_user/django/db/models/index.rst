.. title:: python django models

.. meta::
    :description: 
        Справочная информация по моделям библиотеки django, 
        написанный на языке программирования python,
        для разработки веб приложений.        
    :keywords: 
        python, 
        django, 
        python django, 
        python django models
        django models

.. py:module:: django.db.models

models
======

Миграции, :ref:`django_migrations`.

.. code-block:: py

    from django.db import models

Model
-----

.. py:class:: Model()

    Базовый класс модели

    По умолчанию имеет единственно поле - id.

    .. code-block:: py

        class City(models.Model):

            name = models.CharField(max_length=255)
            state = models.CharField(max_length=255)

            class Meta:
                verbose_name_plural = 'cities'


    .. py:method:: get_absolute_url()

        Возвращает абсолютный путь до объекта

        .. code-block:: py

            from django.core.urlresolvers import reverse

            def get_absolute_url(self):
                return reverse('city:detail', args=[])


    .. py:method:: delete()

        Удаялет модель

        .. code-block:: py

            class Good(models.Model):

                def delete(self, *args, **kwargs):
                    super(Good, self).delete(*args, **kwargs)


    .. py:method:: save()

        Сохраняет модель

        .. code-block:: py

            class Good(models.Model):

                def save(self, *args, **kwargs):
                    super(Good, self).save(*args, **kwargs)

.. toctree::
    :maxdepth: 1

    meta
    fields
    relations
    query