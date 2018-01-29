Глобальные объекты
==================

globals
-------

Глобальная переменная окружения


process
-------

Объект текущего процесса

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


