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

    * **author** - строка, автор модуля
    
        .. code-block:: py

            setup(
                author='ilnurgi'
            )

    * **author_email** - строка, почта автора модуля

        .. code-block:: py

            setup(
                author_email='ilnurgi@email.ru'
            )

    * **description** - строка, описание модуля
    * **entry_points** - соварь, названия точек входа для приложения

        .. code-block:: py

            setup(
                entry_points={
                    'console_scripts': [
                        'snek=snek:main',
                    ],
                    'my_entry_point': [
                        'my_cmd:main',
                    ]
                }
            )

    * **install_requires** - список зависимостей
    
        .. code-block:: py

            setup(
                install_requires=[
                    'selenium',
                ]
            )

    * **name** - строка, название модуля

        .. code-block:: py

            setup(
                name='myapp'
            )

    * **packages** - список пакетов

        .. code-block:: py

            setup(
                packages=setuptools.find_packages(),
            )

    * **py_modules** - список скриптов, которые включает модуль
    * **url** - строка, домашняя страница модуля

        .. code-block:: py

            setup(
                url='http://ilnurgi.ru'
            )

    * **version** - строка, версия модуля

        .. code-block:: py

            setup(
                version='0.5'
            )

.. code-block:: py

    import pkg_resources

    for entry_point in pkg_resources.iter_entry_points('my_entry_point'):        
        callable = entry_point.load()
