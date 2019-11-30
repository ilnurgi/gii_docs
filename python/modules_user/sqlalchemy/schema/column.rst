.. title:: python sqlalchemy column

.. meta::
    :description:
        Справочная информация по python модулю sqlalchemy.schema.
    :keywords:
        python sqlalchemy column

.. py:currentmodule:: sqlalchemy.schema

Column
======

.. py:class:: Column()

    .. code-block:: py

        # индекс - ix_tableName_id
        column = Column('id', Integer, primary_key=True, index=True, unique=True)
        column = Column('name', String, nullable=False)


    .. py:attribute:: name

        Название столбца

        .. code-block:: py
        
            column.name
            # 'id'


    .. py:attribute:: type

        Тип столбца

        .. code-block:: py

            column.type
            # Integer()