psql
====

.. code-block:: sh

	$ psql -p 6432


connect
-------

Подключиться к базу

.. code-block:: sh

	postgres=# \connect ilnurgi_database


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
