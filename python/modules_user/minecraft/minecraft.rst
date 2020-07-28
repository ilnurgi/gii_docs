.. title:: python mcpi minecraft

.. meta::
    :description:
        Справочная информация python, модуль mcpi.minecraft.
    :keywords:
        python mcpi minecraft

.. py:module:: mcpi.minecraft

minecraft
=========

Minecraft()
-----------

.. py:class:: Minecraft()

    Объект для работы с миром minecraft


    .. py:attribute:: camera

        :py:class:`CmdCamera()`


    .. py:attribute:: entity

        :py:class:`CmdEntity()`


    .. py:attribute:: events

        :py:class:`CmdEvents()`


    .. py:attribute:: player

        :py:class:`CmdPlayer()`


    .. py:staticmethod:: create(address, port)

        * **address** - хост, по умолчанию localhost
        * **port** - порт, по умолчанию 4711

        Создает подключение и возвращает инстанс :py:class:`Minecraft`

        .. code-block:: py

            world = Minecraft.create()

            world = Minecraft.create('192.168.0.117', 4712)


    .. py:method:: getBlock(x, y, z)

        Возвращает тип блока

        .. code-block:: py

            world.getBlock(0, 0, 0)
            # 0


    .. py:method:: getBlockWithData(x, y, z)

        Возвращает блок, :py:class:`mcpi.block.Block()`

        .. code-block:: py

            world.getBlockWithData(0, 0, 0)
            # Block(0, 0)


    .. py:method:: getBlocks(x, y, z, dx, dy, dz)

        Возвращает список типов блоков

        .. code-block:: py

            world.getBlocks(0, 0, 0, 1, 1, 1)
            # [0, 0, 0, 31, 0, 0, 0, 0]


    .. py:method:: getHeight(x, z)

        Возвращает высоту мира в точке

        .. code-block:: py

            world.getHeight(0, 0)
            # 100


    .. py:method:: getPlayerEntityId(player_name)

        Возвращает идентификатор игрока по имени

        .. code-block:: py

            world.getPlayerEntityId('ilnurgi')
            # 13018


    .. py:method:: getPlayerEntityIds()

        Возвращает список идентификаторов игроков

        .. code-block:: py

            world.getPlayerEntityIds()
            # [13018]


    .. py:method:: postToChat(message)

        Отправляет сообщение

        .. code-block:: py

            world.postToChat('Hello world')


    .. py:method:: restoreCheckpoint()

        Восстанавливает контрольную точку

        :py:meth:`saveCheckpoint()`

        .. code-block:: py

            world.restoreCheckpoint()


    .. py:method:: saveCheckpoint()

        Сохраняет контрольную точку мира.

        После вызова этого метода, некоторые другие методы валятся с ошибкой.

        :py:meth:`restoreCheckpoint()`

        .. code-block:: py

            world.saveCheckPoint()


    .. py:method:: setBlock(x, y, z, block_type=None, block_sub_type=None)

        Создает новый блок

        .. code-block:: py

            world.setBlock(0, 0, 0, block.DIRT.id)


    .. py:method:: setBlocks(x, y, z, dx, dy, dz, block_type=None, block_sub_type=None)

        Создает блоки

        .. code-block:: py

            world.setBlocks(0, 0, 0, 10, 10, 10, block.STONE.id)


    .. py:method:: settings(setting, status)

        Изменяет настройки мира

        * **world_immutable** - True/False
        * **nametags_visible** - True/False

        .. code-block:: py

            world.setting('world_immutable', True)


CmdPlayer()
-----------

.. py:class:: CmdPlayer()

    Игрок мира, первый по очередности входа на сервер.


    .. py:method:: getDirection()

        Возвращет координату, куда смотри игрок. :py:class:`mcpi.vec3.Vec3()`

        .. code-block:: py

            world.player.getDirection()
            # vec3(-0.237, 0.062, -0.969)


    .. py:method:: getPitch()

        Возвращет угол вертикального обзора игрока, от -90 до 90

        .. code-block:: py

            world.player.getPitch()
            # 12.45


    .. py:method:: getPos()

        Возвращет положение игрока. :py:class:`mcpi.vec3.Vec3()`

        .. code-block:: py

            world.player.getPos()
            # Vec3(81.3,13.3,-20.7)


    .. py:method:: getRotation()

        Возвращет угол горизонтального обзора игрока, от 0 до 360.

        .. code-block:: py

            world.player.getRotation()
            # 84.29


    .. py:method:: getTilePos()

        Возвращет положение чего-то. :py:class:`mcpi.vec3.Vec3()`

        .. code-block:: py

            world.player.getTilePos()
            # Vec3(11, 15, 18)


    .. py:method:: setPos(x, y, z)

        Изменяет положение игрока.

        .. code-block:: py

            player_pos = world.player.getPos()
            world.player.setPos(
                player_pos.x + 10,
                player_pos.y + 10,
                player_pos.z + 10,
            )


    .. py:method:: setting(setting, status)

        Изменяет настройки игрока.

        * **autojump** - True|False

        .. code-block:: py

            world.player.setting('autojump', True)


    .. py:method:: setTilePos(x, y, z)

        Изменяет положение чего-то.

        .. code-block:: py

            player_pos = world.player.getTilePos()
            world.player.setTilePos(
                player_pos.x + 10,
                player_pos.y + 10,
                player_pos.z + 10,
            )


CmdEntity()
-----------

.. py:class:: CmdEntity()

    Сущность мира


    .. py:method:: getDirection(id)

        Возвращет координату, куда смотри объект. :py:class:`Vec3()`

        .. code-block:: py

            world.entity.getDirection(player_id)
            # vec3(-0.237, 0.062, -0.969)


    .. py:method:: getPitch(id)

        Возвращет угол вертикального обзора объекта, от -90 до 90

        .. code-block:: py

            world.entity.getPitch(player_id)
            # 12.45


    .. py:method:: getPos(id)

        Возвращет положение объекта. :py:class:`Vec3`

        .. code-block:: py

            world.entity.getPos(player_id)
            # Vec3(81.3,13.3,-20.7)


    .. py:method:: getRotation(id)

        Возвращет угол горизонтального обзора объекта, от 0 до 360.

        .. code-block:: py

            world.entity.getRotation(player_id)
            # 84.29


    .. py:method:: getTilePos(id)

        Возвращет положение чего-то. :py:class:`Vec3`

        .. code-block:: py

            world.entity.getTilePos(player_id)
            # Vec3(11, 15, 18)


    .. py:method:: setPos(id, x, y, z)

        Изменяет положение объекта. :py:class:`Vec3`

        .. code-block:: py

            player_pos = world.entity.getPos(player_id)
            world.entity.setPos(
                player_id,
                player_pos.x + 10,
                player_pos.y + 10,
                player_pos.z + 10,
            )


    .. py:method:: setting(setting, status)

        Изменяет настройки игрока.

        * **autojump** - True|False

        .. code-block:: py

            world.player.setting('autojump', True)


    .. py:method:: setTilePos(id, x, y, z)

        Изменяет положение чего-то. :py:class:`Vec3`

        .. code-block:: py

            player_pos = world.entity.getTilePos(player_id)
            world.entity.setTilePos(
                player_id,
                player_pos.x + 10,
                player_pos.y + 10,
                player_pos.z + 10,
            )


CmdCamera()
-----------

.. py:class:: CmdCamera()
    
    .. py:method:: setFixed()
    .. py:method:: setFolow(entity_id)
    .. py:method:: setNormal(entity_id)
    .. py:method:: setPos(x, y, z)


CmdEvents()
-----------

.. py:class:: CmdEvents()

    .. py:method:: clearAll()
    .. py:method:: pollBlockHits()
    .. py:method:: pollChatPosts()

        возвращает список сообщений, :py:class:`ChatEvent`

        .. code-block:: py

            world.events.pollChatPosts()
            # [ChatEvent(ChatEvent.POST, 15675, 123123)]
