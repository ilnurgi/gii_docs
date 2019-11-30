.. title:: linux lsof

.. meta::
    :description: 
        Справочная информация по встроенной в linux утилите lsof.
    :keywords: 
        linux lsof

lsof
====

.. code-blocl:: text

    lsof [args] file_path

* args
    
    * -a - компоновщик параметров
    * -c - файлы открытые указанной командой
    * +D - файлы открытые в директории
    * -i - открытые и используемые порты
    * -p - файлы открытые указанным приложением, через пид
    * -u - файлы открытые под пользователем

.. code-blosk:: sh

    # список програма, которые открыли этот файл
    lsof index.html

    lsof -u ilnurgi1, ilnurgi2
    lsof -u ilnurgi1, ilnurgi2

    # файлы открытые пользователями, кроме рута
    lsof -u ^root

    lsof +D /home/ilnurgi/

    lsof -p pid1, pid2, pid3

    # файлы открытые под пользователем используя указанную команду
    lsof -a -u ilnurgi -c comand

    lsof -i
    lsof -i tcp
    lsof -i :8000