.. _django_migrations:

migrations
==========

Консольные утилиты по миграциям данным


makemigrations
--------------

Создание миграции

.. code-block:: sh

    // создаем миграцию для приложения
    python manage.py makemigration app_name

    // создаем миграцию, со своим именем
    python manage.py makemigration app_name --name migration_name

    // создаем пустую миграцию, для ручной миграции например
    python manage.py makemigration app_name --empty


migrate
-------

Запуск миграции

.. code-block:: py

    # мигрируем конкретное приложение
    python manage.py migrate app_name

    # запускаем фейковую миграцию для приложения
    python manage.py migrate app_name --fake


showmigrations
--------------

Просмотр списка миграции

.. code-block:: py

    python manage.py showmigrations app_name


sqlmigrate
----------

Просмотр запроса миграции

.. code-block:: py

    python manage.py sqlmigrate app migration_name


Своя миграция
-------------

Вмиграциях можно использовать следующие операции

* :py:meth:`django.db.migrations.AlterField`
* :py:meth:`django.db.migrations.RunPython`
* :py:meth:`django.db.migrations.RunSql`

.. code-block:: py
    
    from django.db import migrations, models


    def forwards_func(apps, schema_editor):
        """
        функция миграции
        """
        Model = apps.get_model('app_name', 'Model')


    def backwards_func(apps, schema_editor):
        """
        функция отката миграции
        """
        Model = apps.get_model('app_name', 'Model')


    class Migration(migrations.Migration):
        dependencies = [
            ('app_name', '0001_initial'),
        ]
        operations = [
            migrations.RunPython(forwards_func, backwards_func),
            migrations.RunSQL(
                'CREATE INDEX "index_name" ON "app_name" ("field");',
                revert_sql='DROP INDEX "index_name";',
            ),
            migrations.AlterField(
                model_name='model_name',
                name='field_name',
                field=models.DateTimeField(
                    auto_now_add=True,
                    db_index=True,
                ),
            ),
        ]

.. code-block:: py
    
    from django.db import migrations, models


    class Migration(migrations.Migration):

        atomic = False
        # атомарно запустить не получится
        # psycopg2.InternalError: CREATE INDEX CONCURRENTLY cannot run inside a transaction block

        dependencies = [
            ('app_name', '0001_initial'),
        ]

        operations = [

            migrations.SeparateDatabaseAndState(

                state_operations=[
                    migrations.AlterField(
                        model_name='model_name',
                        name='field_name',
                        field=models.DateTimeField(
                            auto_now_add=True,
                            db_index=True,
                        ),
                    ),
                ],

                database_operations=[
                    migrations.RunSQL(
                        'CREATE INDEX CONCURRENTLY "index_name" ON "model_name" ("field_name");',
                        reverse_sql='DROP INDEX "index_name';'
                    ),
                ],
            ),

        ],
