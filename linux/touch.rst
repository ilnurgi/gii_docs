.. title:: linux touch

.. meta::
    :description: 
        Справочная информация по встроенной в linux утилите touch.
    :keywords: 
        linux touch

touch
=====

Создать файл

.. code-block:: text

    $ touch [args] file

* file - путь к файлу

* args
    
    * -a - обновить только дату последнего доступа
    * -c - создать файл если его не существует    
    * -m - обновить только дату изменения
    * -t - модифицировать дату и время создания файла, при его отсутствии, создать файл с указанными датой и временем (YYMMDDhhmm). 

Формат указания даты: [[CC]YY]MMDDhhmm[.ss]

* CC - первые две цифры года
* YY - вторые две цифры года
* MM - месяц
* DD - день
* hh - часы
* mm - минуты
* ss - секунды

.. code-block:: sh
    
    # создать файл
    touch file.txt

    # создать несколько файлов
    touch app.py static/{custom.js,style.css} file-{1..10}.txt

    touch -t 0712250000 filename


