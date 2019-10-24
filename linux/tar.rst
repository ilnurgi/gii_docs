.. title:: linux tar

.. meta::
    :description: 
        Справочная информация по встроенным в linuz утилите tar
    :keywords: 
        linux tar

tar
===

.. code-block:: text

    tar [args] file.tar files

Создать/распаковать tar-архив

* -j - сжатие Bzip
* -c - создать архив
* -x - распаковать
* -z - сжатие Gzip

.. code-block:: sh

    # создать архив
    $ tar -zcvf archive.tar.gz directory/

    $ tar -cv directory | gzip > archive.tar.gz

.. code-block:: sh

    # распаковать архив
    $ tar -zxvf archive.tar.gz

    $ gunzip < archive.tar.gz | tar -xv