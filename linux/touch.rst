touch
=====

touch args file

Создать файл

* args
    
    * -t - модифицировать дату и время создания файла, при его отсутствии, создать файл с указанными датой и временем (YYMMDDhhmm)

* file - путь к файлу

.. code-block:: sh
    
    touch -t 0712250000 filename

    touch app.py static/{custom.js,style.css}
