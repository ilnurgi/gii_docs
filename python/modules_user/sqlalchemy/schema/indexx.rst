.. title:: python sqlalchemy index

.. meta::
    :description:
        Справочная информация по python модулю sqlalchemy.schema.
    :keywords:
        python sqlalchemy index

.. py:currentmodule:: sqlalchemy.schema

Index
=====

.. py:class:: Index()

    .. code-block:: py

        Index('ix_users_ids', user_table.columns.id, user_table.columns.name)
        # CREATE INDEX ix_users_ids ON users (id, name)

        Index('ix_users_ids', user_table.columns.id, unique=True)
        # CREATE UNIQUE INDEX ix_users_ids ON users (id)
        