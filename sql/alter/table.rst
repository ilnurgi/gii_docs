.. title:: sql alter table

.. meta::
    :description:
        Справочная информация по sql, оператор alter table.
    :keywords:
        sql alter table


TABLE
=====

Изменяет структуру таблицы

.. code-block:: text

    ALTER TABLE 
        [<название БД>.]<таблица> 
        <преобразование>




ADD COLUMN
----------

Добавляет новую колонку в таблицу

* новое поле должно иметь дефолтное значение или значение `NULL` должно быть допустимым.
* поле не может быть объявлено как первичный ключ или уникальный

.. code-block:: sql

    ALTER TABLE table_name
    ADD COLUMN group_id INT NOT NULL


ADD FOREIGN KEY
---------------

Добавляет foreign key для таблицы

.. code-block:: sql

	ALTER TABLE table
	ADD FOREIGN KEY (group_id) REFERENCES table_groups (ID)


ALTER COLUMN
------------

Изменяет солбец

.. code-block:: sql

	-- устанавливает дефолтное значение для столбца
	ALTER TABLE table
	ALTER COLUMN group_id SET 1

.. code-block:: sql

	-- усталвнивает новый тип для столбца
	ALTER TABLE table
    ALTER COLUMN group_id UUID



DROP COLUMN
-----------

Удаление столбца из таблицы

.. code-block:: sql

	ALTER TABLE table
	DROP COLUMN group_id



RENAME TO
---------

Переименовывание таблицы

.. code-block:: text

    ALTER TABLE [IF EXISTS] table_name
    RENAME TO new_table_name
 
.. code-block:: sql

    ALTER TABLE table 
    RENAME TO table1


4. ADD
    
    ограничения на таблицу

5. DROP CONSTRANT <столбец> RESTRICT | CASSCADE