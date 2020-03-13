.. title:: python setuptools

.. meta::
    :description:
        Справочная информация по python модулю setuptools.
    :keywords:
        python setuptools

setuptools
==========

.. warning::

    Добавлено в python 3.4


.. code-block:: sh

    # создание файла установщика
    # на винде создаст .zip архив
    # в unix системах .tar.gz
    python setup.py sdist


setup()
-------

.. py:method:: setup(**kwargs)

    * **entry_points** - соварь, названия точек входа для приложения
    * **name** - строка, название модуля
    * **version** - строка, версия модуля
    * **description** - строка, описание модуля
    * **author** - строка, автор модуля
    * **author_email** - строка, почта автора модуля
    * **url** - строка, домашняя страница модуля
    * **py_modules** - список скриптов, которые включает модуль

    .. code-block:: py

        from setuptools import setup

        setup(
            name=myapp,
            entry_points={
                    'console_scripts': [
                        'snek=snek:main',
                    ],
                    'my_entry_point': [
                        'my_cmd:main',
                    ]
            }
        )

    .. code-block:: py

        import pkg_resources

        for entry_point in pkg_resources.iter_entry_points('my_entry_point'):        
            callable = entry_point.load()
