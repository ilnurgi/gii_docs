.. py:module:: glob

glob
====

Поиск файлов по паттернам

.. code-block:: py

    import glob
    

.. py:function:: glob()

    .. code-block:: py

        for file_name in glob.glob('*.txt'):
            # ...

glob.glob1(dirname, pattern)

::

    glob.glob1('c://', '*.exe')