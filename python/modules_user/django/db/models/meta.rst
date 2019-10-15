Метаданные
==========

.. code-block:: py

    class Good(models.Model):

        class Meta:

            db_table = 'db_table'
            ordering = ['id', '-date']
            unique_together = ['name', 'date']
            verbose_name = ''
            verbose_name_plural = ''
            permissions = (
                ("can_some", "titile"),
            )
            indexes = [
                models.Index(fields=['-pub_date'])
            ]


db_table
--------

Строка, имя таблицы. По умолчанию - имяПриложения_имяТаблицы

indexes
-------

Расширенная настройка индексов модели

.. code-block:: py

    # индекс для одного поля, с сортировкой desc
    indexes = [
        models.Index(fields=['-pub_date'], name='index_name')
    ]


ordering
--------

Список полей, сортировка по умолчанию


.. _models_meta_permissions:

permissions
-----------

Список прав, отличных от тех что пердоставляет модуль :ref:`django_contrib_auth`

Право должно начинаться с суффикса `can_`


unique_together
---------------

Список полей, значения которых должны быть уникальны


verbose_name
------------

Строка, название модели


verbose_name_plural
-------------------

Строка, название модели во множественном числе. 
