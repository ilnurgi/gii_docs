.. title:: python importlib metadata

.. meta::
    :description: 
        Справочная информация по python модулю importlib.metadata.
    :keywords: 
        python importlib metadata

.. py:module:: importlib.metadata

metadata
========

.. versionadded:: 3.8

files()
-------

.. py:function:: files(module_name)

    Возвращает список :py:class:`pathlib.Path()` всех файлов модуля

    .. code-blog:: py

        metadata.files('pip')
        # ['file', ...]


metadata()
----------

.. py:function:: metadata(module_name)

    Возвращает сведения по модулю

    .. code-blog:: py

        metadata.metadata('pip')
        """
        {
            'Name': '',
            'Version': '',
            ....
        }
        'Metadata-Version', 'Name', 'Version', 'Summary', 'Home-page', 'Author',
        'Author-email', 'License', 'Keywords', 'Platform', 'Classifier',
        'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier',
        'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier',
        'Classifier', 'Classifier', 'Requires-Python'
        """


requires()
----------

.. py:function:: requires(module_name)

    Возвращает список зависимостей модуля

    .. code-blog:: py

        metadata.requires('some-module')
        # ['requests', ...]


version()
---------

.. py:function:: version(module_name)

    Возвращает версию модулю

    .. code-blog:: py

        metadata.version('pip')
        # '19.2.3'