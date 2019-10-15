.. title:: python module zipfile

.. meta::
    :description: 
        Справочная информация по модулю zipfile, python.    
    :keywords: 
        python,
        python zipfile

.. py:module:: zipfile

zipfile
=======

ZipFile()
---------

.. py:class:: ZipFile(file, mode)
    
    объект архив

    .. code-block:: py

        from io import BytesIO

        in_memory_zip = BytesIO(some_content)
        with ZipFile(in_memory_zip) as zippy:
            for item in zippy.infolist():
                if 'Exports' in item.filename:
                    with zippy.open(item.filename) as export_file:
                        for row in export_file:
                            print(row.decode('utf-8'))
                            

    .. py:method:: write(src, localpath)

        добавляет в архив файл

        :param str src: путь к файлу
        :param str localpath: путь файла в архиве


    .. py:method:: read(path)

        читает файл из архива, возвращает данные в бинарном формате

        :param str path: путь к файлу


    .. py:method:: namelist()

        возвращает список строк, путей к файлам архива