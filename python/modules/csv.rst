.. title:: python module csv

.. meta::
    :description: 
        Справочная информация по модулю csv, python.    
    :keywords: 
        python,
        python csv

.. py:module:: csv

csv
===

.. code-blcok:: py

    from io import StringIO, BytesIO
    import csv

    in_memory_file = StringIO()
    csv_writer = csv.writer(in_memory_file)
    csv_writer.writerows([[1, 2, 3], [4, 5, 6]])
    in_memory_file.seek(0)
    for row in in_memory_file:
        print(row)