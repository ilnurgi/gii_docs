.. title:: postgres psql

.. meta::
    :description:
        Справочная информация по работе в psql.
    :keywords:
        postgres psql

psql
====

.. code-block:: sh

	$ psql -p 6432


connect
-------

Подключиться к базу

.. code-block:: sh

	postgres=# \connect ilnurgi_database


d
-

Сведения по таблице

.. code-block:: sh

	postgres=# \d table_name;

	Column | Type    | Modifiers
	-------+---------+----------
	id     | integer | not null
	Indexes:
	Foreign-key constraints:


dt
--

Список таблиц в текущей БД

.. code-block:: sh

	postgres=# \dt
	List of relations
	Shema  | Name     | Type  | Owner
	-------+----------+-------+---------
	public | sessions | table | postgres


list
----

Список существующих баз

.. code-block:: sh

	postgres=# \list
    List of databases
   	Name      |  Owner   
	----------+----------
 	postgres  | postgres 
 	template0 | postgres 
 	template1 | postgres 
