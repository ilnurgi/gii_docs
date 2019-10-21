.. title:: linux scp

.. meta::
    :description: 
        Справочная информация по встроенной в linux утилите scp.
    :keywords: 
        linux scp,
        scp

scp
===

Копирует папки/файлы между машинами

.. code-block:: text

    scp [kwargs] src dst

* src - путь, откуда копируем

* dst - путь, куда копируем

* kwargs
  
  * -С - копирование с архивированием
  * -p - сохранить мета информацию о файле при копировании
  * -P - port - порт подключения
  * -r - рекурсивно файлы и папки
  * -v - вывод сведений при копировании
    
.. code-block:: sh

    # копируем файл с локальной машины на удаленную
    $ scp /home/user/some.txt user@ip_address:/home/user/some.txt

    # копируем файл с удаленной машины на локальную
    $ scp user@ip_address:/home/user/some.txt /home/user/some.txt

    # копирование файлов между двумя удаленными машинами
    $ scp user@ip_address1:/home/user/some.txt user@ip_address1:/home/user/some.txt

    # копируем несколько файлов с локальной машины на удаленную
    $ scp /home/user/some.txt /home/user/some2.txt user@ip_address:/home/user/some.txt

    # копируем папку с локальной машины на удаленную
    $ scp -r /home/user/ user@ip_address:/home/user/