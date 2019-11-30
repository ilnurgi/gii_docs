.. title:: python os.path

.. meta::
    :description:
        Справочная информация по python модулю os.path.
    :keywords:
        python os.path

.. py:module:: os.path

path
====

Модуль встроен в модуль os и позволяет работать с путями к файлам и папкам


abspath()
---------

.. py:method:: abspath(path)

    возвращает полный путь до папки/файла

    .. code-block:: py

        os.path.abspath("1.txt")
        '/home/ilnurgi/1.txt'


basename()
----------

.. py:method:: basename(path)

    Возвращает строку, имя файла или папки.

    .. code-block:: py

        os.path.basename('c:\\system\\apps\\Python\\Python.app')
        'Python.app'


dirname()
---------

.. py:method:: dirname(path)

    Возвращает строку, путь к родительской папки файла

    .. code-block:: py

        os.path.dirname ('c:\\system\\apps\\Python\\Python.app')
        'c:\\system\\apps\\Python'


exists()
--------

.. py:method:: exists(path)

    Возвращает булево, True|False, существует ли указанный путь в системе

    .. code-block:: py

        os.path.exists(u'/home/ilnurgi/')
        True


expanduser()
------------

.. py:method:: expanduser(username)

    * username - :py:class:`str`, имя пользователя

    Возвращает путь к пользовательской папке

    .. code-block:: py

        expanduser('~')
        'c:\\users\\ilnurgi\\'


getatime()
----------

.. py:method:: getatime(path)

    Возвращает время последнего доступа к файлу или папке, в виде количесвта секунд, прошедших с начала эпохи.


getctime()
----------

.. py:method:: getctime(path)

    Возвращает дату создания файла или папки, в виде количества секунд, прошедших с начала эпохи


getmtime()
----------

.. py:method:: getmtime(path)

    Возвращает время последнего внесения изменения в файл или папку,
    в виде количесвта секунд, прошедших с начала эпохи


getsize()
---------

.. py:method:: getsize(path)

    Возвращает размер файла или папки


join()
------

.. py:method:: join(path1, path3,...)

    Объединяет пути.

    .. code-block:: py

        os.path.join('c:\\', 'system\\apps\\Python\\', 'Python.app')
        'c:\\system\\apps\\Python\\Python.app'


isabs()
-------

.. py:method:: isabs(path)

    проверяет путь на абсолютность


isdir()
-------

.. py:method:: isdir(path)

    Возвращает булево, True|False, является ли указанный путь катологом

    .. code-block:: py

        os.path.isdir(u'/home/ilnurgi/')
        True


isfile()
--------

.. py:method:: isfile(path)

    проверяет, указывает ли путь к файлу


islink()
--------

.. py:method:: islink(path)

    проверяет, указывает ли путь к символической ссылке

    .. code-block:: py

        os.path.islink("path1/1.txt")
        True


normpath()
----------

.. py:method:: normpath(path)

    возвращает строку, нормальизованный путь согласно операционной системы

    .. code-block:: py

        р = os.path.join(r"C:\\", "book/folder/", "file.txt")
        os.path.normpath(p)
        # 'C:\\book\\folder\\file.txt'


realpath()
----------

.. py:method:: realpath(path)

    Возвращает путь к файлу символьной ссылки

    .. note:: linux

    .. code-block:: py

        os.path.realpath("symlink_path")
        "real_path"


split()
----------

.. py:method:: split(path)

    Возвращает кортеж из пары строк - (путь к родителской папке, название файла).

    .. code-block:: py

        os.path.split('c:\\system\\apps\\Python\\Python.app')
        ('c:\\system\\apps\\Python\\', 'Python.app')


splitdrive()
------------

.. py:method:: splitdrive(path)

    Возвращает кортеж из пары строк - (имя диска, остальная часть пути).

    .. code-block:: py

        os.path.splitdrive ('c:\\system\\apps\\Python\\Python.app')
        ('c:\\', 'system\\apps\\Python\\Python.app')


splitext()
----------

.. py:method:: splitext(path)

    Возвращает кортеж из пары строк - (путь к файлу без расширения, расширение файла)

    .. code-block:: py

        os.path.splitext ('c:\\system\\apps\\Python\\Python.app')
        ('c:\\system\\apps\\Python\\Python', '.app')


walk()
------

.. py:method:: walk(path, visit, arg)

    Вызывает функцию 'visit' передавая ей параметры

    .. note:: в 3 ветке перенесен в модуль :py:mod:`os`

    .. code-block:: py

        def listfiles(arg ,dirname , fnames):
            print dirname
        os.path.walk('e:\\python\\, listfiles, None)
