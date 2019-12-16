.. title:: python os

.. meta::
    :description:
        Справочная информация по python модулю os.
    :keywords:
        python os

.. py:module:: os

os
==

Модуль позволяет работать с файлами и папками.

Русские названия файлов и папок возвращаются и
принимаются всеми функциями этого модуля в кодировке UTF-8,
поэтому необходимо использовать функции для перекодирования строк -
методы decode и encode.

.. toctree::
    :maxdepth: 1

    path

name
----

.. py:attribute:: name

    название версии модуля, зависит от операционной системы

    .. code-block:: py

        os.name
        # 'nt' - windows xp


environ
-------

.. py:attribute:: environ

    Словарь переменных окружения

    .. code-block:: py

        os.environ
        """
        {
            'HOME': 'c:\\',
        }
        """


access()
--------

.. py:method:: access(<путь>, <режим>)

    проверка прав доступа к файлу или папке.

    В параметре режим могут быть указаны следующие константы:

    * os.F_OK - проверка наличия пути
    * os.R_OK - проверка на возможность чтения
    * os.W_OK - проверка на возможность записи
    * os.X_OK - проверка на возможность выполнения


chdir()
-------

.. py:method:: chdir(path)

    :param str path: путь к каталогу

    Изменяет текущий рабочий каталог приложения на указанный


chmod()
-------

.. py:method:: chmod(path, mode)

    Изменяет права доступа файла.

    .. code-block:: py

        import stat

        os.chmod('file.txt', 0o777)
        os.chmod('file.txt', stat.s_IRUSR)


chown()
-------

.. py:method:: chown(path, uid, gid)

    Изменят владельца файла

    .. note:: linux

    .. code-block:: py

        os.chown('file.txt', 5, 22)


getcwd()
--------

.. py:method:: getcwd()

    Возвращает рабочий путь приложения

    .. code-block:: py

        os.getcwd()
        # 'c:\\'


getenv()
--------

.. py:method:: getenv(env_param_name)

    Возвращает значение переменной окружения

    .. code-block:: py

        os.getenv('HOME')
        # 'c:\\'


link()
--------

.. py:method:: link(src, dst)

    Создает жесткую ссылку (linux)

    .. code-block:: py

        os.link("path1/1.txt", "path2/1.txt")


listdir()
---------

.. py:method:: listdir(path)

    Возвращает список имен файлов и папок в указанной папке

    .. code-block:: py

        os.listdir('/home/ilnurgi/')
        # ['.bashrc']


mkdir()
--------

.. py:method:: mkdir(path[, access=0o777])

    * path - путь к каталогу
    * access - права доступа

    Создает папку по указанному пути


makedirs()
----------

.. py:method:: makedirs(path)

    Аналогичен функции .. py:method::'mkdir',
    но автоматический создает промежуточные папки


remove()
--------

.. py:method:: remove(path)

    Удаляет файл

    Возбуждает исключение :py:class:`WindowsError`, если файл удалить нельзя

    .. code-block:: py

        os.remove("1.txt")


rmdir()
-------

.. py:method:: rmdir(path)

    :param str path: путь к каталогу

    Удаляет папку по указанному пути


removedirs()
------------

.. py:method:: removedirs(path)

    Аналогичен функции rmdir, но автоматический удаляет все родительские пустые папки


rename()
--------

.. py:method:: rename(src, dst)

    * src - исходный путь
    * dst - путь назначения

    Переименовывает файл

    Возбуждает исключение :py:class:`WindowsError` - если файл не удалось найти
    или новый файл уже существует

    .. code-block:: py

        os.rename("path1/1.txt", "path2/1.txt")


symlink()
---------

.. py:method:: symlink(src, dst)

    Создает символическую ссылку (linux)

    .. code-block:: py

        os.symlink("path1/1.txt", "path2/1.txt")


system()
--------

.. py:method:: system(command)

    Выполняет команду в терминале

    .. code-block:: py

        os.system('echo ilnurgi')
        # ilnurgi

        exit_code = os.system('cd ~')
        # 0

        exit_code = os.system('cd blablalba')
        # 256


stat()
------

.. py:method:: stat(path)

    Возвращает состояние о файле, объект stat_result, который в зависимости от типа операционной системы содержит разные атрибуты.


tempname()
----------

.. py:method:: tempname([path, [prefix]])

    Возвращает уникальный путь для создания временных файлов.


unlink()
--------

.. py:method:: unlink(path)

    :param path: путь к файлу
    :raises WindowsError: если файл удалить не удалось

    удаляет файл


utime()
-------

.. py:method:: utime(path[, (atime=now, mtime=now)])

    :param str path: путь к файлу
    :param int atime: время последнего доступа в секндах
    :path int mtime: время изменения в секундах
    :raises WindowsError: если файл не найден

    обновляет время последнего достпуа и время изменения


walk()
------

.. py:method:: walk(path[, topdown=True][, onerror=None][, followlinks=False])

    :param str path: путь к начальному каталогу
    :param bool topdown: задает последовательность обхода каталогов

    Возвращает итератор, на каждой итерации возвращает кортеж (текущий каталог, список каталогов и список файлов)


close()
-------

.. py:method:: close(<дескриптор>)

    закрывает файл


dup()
-----

.. py:method:: dup(<дескриптор>)

    возвращает дубликат дескриптора


fdopen()
--------

.. py:method:: fdopen(<дескриптор>[, <режим>[, <размер буфера>]])

    возвращает файловый объект по указанному дескриптору


lseek()
-------

.. py:method:: lseek(<дескриптор>, <смещение>, <позиция>)

    устанавливает указатель в позицию, имеюущий указанное смещение относительной указанной позиции

    в параметре позици могут быть указаны следующие значения:

    * os.SEEK_SET или 0 - начало файла
    * os.SEEK_CUR или 1 - текущая позиция укзаталея
    * os.SEEK_END или 2 - конец файла


open()
------

.. py:method:: open(<путь к файлу>, <режим>[, mode=0o777])

    Открывает файл и возвращает целочисленный дескриптор

    В параметре <режим> в операционной системе windows
    могут быть указаны следующие флаги (или их комбинации через символ \|):

    * os.O_RDONLY - чтение
    * os.O_WRONLY - запись
    * os.O_RDWR - чтение и запись
    * os.O_APPEND - добавление в конец файла
    * os.O_CREATE - создать файл, если он не существует
    * os.O_TRUNC - очистить содержимое файла
    * os.O_BINARY - файл будет открыт в бинарном режиме
    * os.O_TEXT - файл будет открыт в текстовом режиме


read()
------

.. py:method:: read(<дескриптор>, <количество байтов>)

    читает из файла указанное количество байтов


write()
-------

.. py:method:: write(<дескриптор>, <последовательность байтов>)

    записывает последовательность байтов в файл
