Глобальные объекты
==================

__dirname
---------

Путь к текущей папке, откуда запущен скрипт

.. code-block:: js

    console.log(__dirname);
    // c:\projects\


__filename
---------

Путь к текущему файлу

.. code-block:: js

    console.log(__filename);
    // c:\projects\ilnurgi.js

globals
-------

Глобальная переменная окружения


process
-------

Объект текущего процесса

argv
++++

Массив переданных параметров скрипту

.. code-block:: js

    process.argv
    // ['node', 'script.js', 'param1']


env
+++

Переменные окружения

stdin
+++++

Поток ввода процесса

.. code-block:: js

    process.stdin.pipe()


stdout
++++++

Выходной поток процесса

.. code-block:: js

    process.stdout.write('hello world');


chdir()
+++++++

Меняет  рабочию директорию

.. code-block:: js

    process.chdir('my_folder');


cwd()
+++++

Возвращает рабочую директорию

.. code-block:: js

    process.cwd()


