.. title:: python mcpi event

.. meta::
    :description:
        Справочная информация python, модуль mcpi.event.
    :keywords:
        python mcpi event

.. py:module:: mcpi.event

event
=====

BlockEvent()
------------

.. py:class:: BlockEvent()

    .. py:attribute:: HIT
    .. py:attribute:: type
    .. py:attribute:: pos
    .. py:attribute:: face
    .. py:attribute:: entityId

    .. py:staticmethod:: Hit(x, y, z, face, entityId)


ChatEvent()
-----------

.. py:class:: ChatEvent()

    .. code-block:: py

        ChatEvent(ChatEvent.POST, 15675, 'message')

    .. py:attribute:: POST
    .. py:attribute:: type
    .. py:attribute:: message
    .. py:attribute:: entityId

    .. py:staticmethod:: Post(entityId, message)
