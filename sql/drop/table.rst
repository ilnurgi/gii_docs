.. title:: sql drop table

.. meta::
    :description: 
        Справочная информация по субд postgres, drop table.
    :keywords: 
        sql drop table

DROP TABLE
==========

Удаляет таблицу

.. code-block:: text
    
    DROP TABLE [IF EXISTS] table_name [RESTRICT | CASSCADE]
    
* **CASSCADE** - удаляет зависимые записи
* ***RESTRICT** - не удаляет таблицу если есть зависимости