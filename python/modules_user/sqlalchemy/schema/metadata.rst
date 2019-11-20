.. title:: python sqlalchemy metadata

.. meta::
    :description:
        Справочная информация по python модулю sqlalchemy.schema.
    :keywords:
        python sqlalchemy metadata

.. py:currentmodule:: sqlalchemy.schema

MetaData
========

.. py:class:: MetaData()

    .. code-block:: py

        meta = MetaData()

    .. py:attribute:: tables

        Список таблиц базы, зарегистрированные в объекте.


    .. py:method:: create_all()

        Создает все таблицы

        .. code-block:: py

            engine = create_engine('sqlite://')
            metadata.create_all(engine)


    .. py:method:: reflect()

        Загружает все данные по таблицам из базы и возвращает её

        .. code-block:: py

            meta.reflect(bind=engine)
