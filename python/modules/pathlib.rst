.. py:module:: pathlib

pathlib
=======

.. versionadded:: python 3.4

.. code-block:: py

    import pathlib


Path()
------

.. py:class:: Path()

    .. code-block:: py

        from pathlib import Path

        Path(r'C:\Users\ilnurgi\test.txt')
        # WindowsPath('C:/Users/ilnurgi/test.txt')

        path = Path.home() / 'ilnurgi.txt'
        # PosixPath('/home/ilnurgi/ilnurgi.txt')

        with path.open(mode='r') as f:
            pass


    .. py:attribute:: anchor

        

        .. code-block:: py 

            Path.home().anchor
            # '/'

            # windows
            Path('c:/Program Files/').anchor
            # 'c:\\'

            # windows
            Path('c:Program Files/').anchor
            # 'c:'

            # windows
            Path('//host/share').anchor
            # '\\\\host\\share\\'


    .. py:attribute:: drive
        
        .. code-block:: py 

            # windows
            Path('c:/Program Files/').drive
            # 'c:'
            
            # windows
            Path('/Program Files/').drive
            # ''

            # windows
            PureWindowsPath('//host/share/foo.txt').drive
            # '\\\\host\\share'

            Path('/etc').drive
            # ''


    .. py:attribute:: name

        Имя файла без пути, но с расширением

        .. code-block:: py 

            Path.home().name
            # ilnurgi


    .. py:attribute:: parent

        Родительская папка объекта

        .. code-block:: py

            Path.home().parent
            # PosixPath('/home')


    .. py:attribute:: parents

        Возвращает список родителей 

        .. code-block:: py

            Path.home().parents
            """
            [
                Path('/home'),
                Path('/'),
            ]
            """


    .. py:attribute:: parts

        Возвращает кортеж пути

        .. code-block:: py

            Path.home().parts
            # ('/', 'home', 'ilnurgi')

            # windows
            Path.home().parts
            # ('c:\\', 'Users', 'ilnurgi')


    .. py:attribute:: root

        Корень пути

        .. code-block:: py

            # windows
            Path('c:/Program Files/').root
            # '\\'

            # windows
            Path('c:Program Files/').root
            # ''

            # windows
            Path('//host/share').root
            # '\\'

            PurePosixPath('/etc').root
            '/'

    .. py:attribute:: stem

        Имя файла без расширения

        .. code-block:: py

            (Path.home() / 'ilnurgi.txt').stem
            # 'ilnurgi'


    .. py:attribute:: suffix

        Расширение файла

        .. code-block:: py

            (Path.home() / 'ilnurgi.txt').suffix
            # '.txt'


    .. py:attribute:: suffixes

        Расширение файла

        .. code-block:: py

            (Path.home() / 'ilnurgi.tar.gz').suffixes
            # ('.tar', '.gz')


    .. py:method:: as_posix()

        Возвращает путь в формате posix

        .. code-block:: py

            Path('c:\\windows').as_posix()
            # 'c:\\windows'


    .. py:method:: as_uri()

        Возвращает путь в формате URI

        .. code-block:: py

            Path('/etc/passwd').as_uri()
            # 'file:///etc/passwd'
            
            Path('c:/Windows').as_uri()
            # 'file:///c:/Windows'


    .. py:method:: chmod(mod)

        Меняет права, также как и :py:meth:`os.chmod()`

        .. code-block:: py

            Path('setup.py').stat().st_mode
            # 33277
            
            Path('setup.py').chmod(0o444)

            Path('setup.py').stat().st_mode
            # 33060


    .. py:method:: cwd()

        Возвращает путь до рабочей директории

        .. code-block:: py

            Path.cwd()
            # PosixPath('/home/ilnurgi/')


    .. py:method:: exists()

        Существует ли путь

        .. code-block:: py

            Path.home().exists()
            # True


    .. py:method:: expanduser()

        .. versionadded:: python 3.5

        Путь до домашней папки пользователя, :py:meth:`os.path.expanduser()`

        .. code-block:: py

            Path.cwd().expanduser()
            # '/home/ilnurgi/'


    .. py:method:: glob(pattern)

        Возвращет все файлы по вхождению

        .. code-block:: py

            Path.home().glob('*.py')
            # ['ilnurgi.py']


    .. py:method:: group()

        Возвращает имя группы владельца пути

        .. code-block:: py

            Path.home().group
            # 'ilnurgi_group'


    .. py:method:: home()

        .. versionadded:: python 3.5

        Возвращает путь до домашней папки пользователя

        .. code-block:: py

            Path.home()
            # PosixPath('/home/ilnurgi')


    .. py:method:: is_absolute()

        Является ли путь абсолютным

        .. code-block:: py

            Path.home().is_absolute()
            # True


    .. py:method:: is_block_device()

        .. code-block:: py

            Path.home().is_block_device()
            # False


    .. py:method:: is_char_device()

        .. code-block:: py

            Path.home().is_char_device()
            # False


    .. py:method:: is_dir()

        Путь является папкой

        .. code-block:: py

            Path.home().is_dir()
            # True


    .. py:method:: is_fifo()

        .. code-block:: py

            Path.home().is_fifo()
            # False


    .. py:method:: is_file()

        Путь является файлом

        .. code-block:: py

            Path.home().is_file()
            # False


    .. py:method:: is_mount()

        Путь является примонтированным объектом

        .. code-block:: py

            Path.home().is_mount()
            # False


    .. py:method:: is_reserved()

        Является ли путь зарезервированным, актуально для windows

        .. code-block:: py

            PureWindowsPath('nul').is_reserved()
            # True


    .. py:method:: is_socket()

        Является ли путь сокетом

        .. code-block:: py

            Path.home().is_socket()
            # False


    .. py:method:: is_symlink()

        Является ли путь симлинком

        .. code-block:: py

            Path.home().is_symlink()
            # False


    .. py:method:: iterdir()

        Возвращает генератор, списко объектов в директории

        .. code-block:: py

            for i in Path.home().iterdir():
                print(i)
            
            # PosixPath('/home/ilnurgi/ilnurgi.txt')
            # ...


    .. py:method:: joinpath(*other)

        Объединяет пути

        .. code-block:: py

            Path.home().joinpath('ilnurgi.txt')
            # '/home/ilnurgi/ilnurgi.txt'


    .. py:method:: lchmod(mode)

        Также как и :py:meth:`Path.chmod` меняет права и для символьных ссылок тоже

        .. code-block:: py

            Path('setup.py').lchmod(0o444)


    .. py:method:: lstat()

        Возвращает сведения по пути, :py:meth:`os.stat()` и для сивольных ссылок

        .. code-block::py

            Path('setup.py').stat().st_size
            # 956


    .. py:method:: match(pattern)
        
        .. code-block:: py

            Path.home().joinpath('ilnurgi.txt').match('*.txt')
            # True


    .. py:method:: mkdir(mode=0o777, parents=False, exist_ok=False)

        Создает файл по указанному пути

        .. code-block:: py

            (Path.home() / 'ilnurgi').mkdir()


    .. py:method:: open()

        Открывает и возвращает файловый дескриптор

        .. code-block:: py

            with Path('setup.py').open() as f:
                ...


    .. py:method:: owner()

        Возвращает автора файла

        .. code-block:: py

            Path.home().owner()
            # 'ilnurgi'


    .. py:method:: read_bytes()

        .. versionadded:: python 3.5
        
        Читает и возвращает байтовое содержимое объекта

        .. code-block:: py

            (Path.home() / 'ilnurgi.txt').read_bytes()
            # b'Hello ilnurgi!'


    .. py:method:: read_text(encoding=None, errors=None)

        .. versionadded:: python 3.5

        Читает и возвращает строковое содержимое объекта

        .. code-block:: py

            (Path.home() / 'ilnurgi.txt').read_text()
            # 'Hello ilnurgi!'


    .. py:method:: relative_to(*other)

        .. code-block:: py

            PurePosixPath('/etc/passwd').relative_to('/')
            # PurePosixPath('etc/passwd')
            
            PurePosixPath('/etc/passwd').relative_to('/etc')
            # PurePosixPath('passwd')
            
            PurePosixPath('/etc/passwd').relative_to('/usr')
            """
            Traceback (most recent call last):
              File "<stdin>", line 1, in <module>
              File "pathlib.py", line 694, in relative_to
                .format(str(self), str(formatted)))
            ValueError: '/etc/passwd' does not start with '/usr'
            """


    .. py:method:: rename(target)

        Переименовывает объект по пути

        .. code-block:: py

            (Path.home() / 'ilnurgi.txt').rename('ilnurgi.log')


    .. py:method:: resolve(strict=False)

        .. versionadded:: параметр strict добавлен python 3.6

        Возвращает полный путь до объекта

        .. code-block:: py

            Path.home().resolve()
            # PosixPath('/home/ilnurgi/')


    .. py:method:: rglob(pattern)

        Рекурсивный обход пути по поиску объектов

        .. code-block:: py

            sorted(Path().rglob("*.py"))
            """
            [
                PosixPath('build/lib/pathlib.py'),
                PosixPath('docs/conf.py'),
                PosixPath('pathlib.py'),
                PosixPath('setup.py'),
                PosixPath('test_pathlib.py')
            ]
            """

    .. py:method:: rmdir()

        Удаляет папку по пути, папка должна быть пустая

        .. code-block: py

            (Path.home() / 'ilnurgi').rmdir()
    

    .. py:method:: samefile()

        .. versionadded:: python 3.5


    .. py:method:: stat()

        Возвращает сведения по пути, :py:meth:`os.stat()`

        .. code-block::py

            Path('setup.py').stat().st_size
            # 956


    .. py:method:: symlink_to(target, target_is_directory=False)

        Создает симлинк по указанному `target`

        .. code-block:: py

            Path.home().symlink_to(Path.home() / 'home_ilnurgi')

    
    .. py:method:: touch(mode=0o666, exist_ok=True)

        Создает файл по указанному пути

        .. code-block:: py

            (Path.home() / 'ilnurgi.txt').touch()


    .. py:method:: unlink(name)

        Удаляет файл или символическую ссылку.

        
    .. py:method:: with_name(name)

        Меняет имя у пути

        .. code-block:: py

            (Path.home() / 'ilnurgi.txt').with_name('ilnurgi.log')
            # PosixPath('/home/ilnurgi/ilnurgi.log')


    .. py:method:: with_suffix(suffix)

        Меняет расширение у файла

        .. code-block:: py

            (Path.home() / 'ilnurgi.txt').with_suffix('.log')
            # PosixPath('/home/ilnurgi/ilnurgi.log')


    .. py:method:: write_bytes(data)

        .. versionadded:: python 3.5
        
        Записывает байты данных в файл

        .. code-block:: py

            (Path.home() / 'ilnurgi.txt').write_bytes(b'Hello ilnurgi!')
            # 10


    .. py:method:: write_text(data, encoding=None, errors=None)

        .. versionadded:: python 3.5

        Записывает строковые данные в файл

        .. code-block:: py

            (Path.home() / 'ilnurgi.txt').write_text('Hello ilnurgi!')
            # 20
