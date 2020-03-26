.. title:: python modules

.. meta::
    :description: 
        Справочная информация по python, модули.
    :keywords: 
        python modules

Модули
======

.. code-block:: py

    # импорт модуля
    import os

    # словарь, содержащий атрибуты модуля
    os.__dict__ 
    {
        'PathLike': 'os.PathLike'
    }

    # строка документирования модуля
    os.__doc__
    'OS ....'

    # имя модуля
    os.__name__
    'os'

    # имя файла, откуда был загружен модуль
    os.__file__
    'c:\\python374\\lib\\os.py'

    # полное имя пакета
    # определен, только когда объект модуля ссылается на пакет
    os.__path__
    "AttributeError: ..."
