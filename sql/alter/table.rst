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


ADD CONSTRAINT
--------------

.. code-block:: text

    ALTER TABLE table_name
    ADD CONSTRAINT constraint_name constraint_definition


ADD FOREIGN KEY
---------------

Добавляет foreign key для таблицы

.. code-block:: sql

	ALTER TABLE table_name
	ADD FOREIGN KEY (column_name) REFERENCES reference_table_name (reference_column_id)


ALTER COLUMN
------------

Изменяет солбец

.. code-block:: text

    ALTER TABLE table
    ALTER COLUMN column [SET DEFAULT value | DROP DEFAULT];

    ALTER TABLE table
    ALTER COLUMN column [SET NOT NULL | DROP NOT NULL];

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



RENAME COLUMN
-------------

Переименовывание столбца

.. code-block:: sql

    ALTER TABLE table_name
    RENAME COLUMN column_name TO new_column_name


RENAME TO
---------

Переименовывание таблицы

.. code-block:: text

    ALTER TABLE [IF EXISTS] table_name
    RENAME TO new_table_name
 
.. code-block:: sql

    ALTER TABLE table 
    RENAME TO table1
