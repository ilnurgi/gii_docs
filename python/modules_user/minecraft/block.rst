.. title:: python mcpi block

.. meta::
    :description:
        Справочная информация python, модуль mcpi.block.
    :keywords:
        python mcpi block

.. py:module:: mcpi.block

block
=====

Block()
-------

.. py:class:: Block()

    .. code-block:: py

        block = Block(id)
        block = Block(id, data)

.. py:class:: AIR

    .. code-block:: py
        
        Block(0)


.. py:class:: STONE

    .. code-block:: py
        
        Block(1)


.. py:class:: GRASS

    .. code-block:: py
        
        Block(2)


.. py:class:: DIRT

    .. code-block:: py
        
        Block(3)


.. py:class:: COBBLESTONE

    .. code-block:: py
        
        Block(4)


.. py:class:: WOOD_PLANKS

    .. code-block:: py
        
        Block(5)

    data-types (Not on Pi)

    * **0** - Oak
    * **1** - Spruce
    * **2** - Birch
    * **3** - Jungle


.. py:class:: SAPLING

    .. code-block:: py
        
        Block(6)

    data-types

    * **0** - Oak
    * **1** - Spruce
    * **2** - Birch
    * **3** - Jungle (Not on Pi)


.. py:class:: BEDROCK

    .. code-block:: py
        
        Block(7)


.. py:class:: WATER_FLOWING

    .. code-block:: py
        
        Block(8)


.. py:class:: WATER

    .. code-block:: py
        
        WATER_FLOWING


.. py:class:: WATER_STATIONARY

    .. code-block:: py

        Block(9)

    data-types

    0-7: Level of the water, 0 being the highest, 7 the lowest


.. py:class:: LAVA_FLOWING

    .. code-block:: py

        Block(10)


.. py:class:: LAVA

    .. code-block:: py

        LAVA_FLOWING


.. py:class:: LAVA_STATIONARY

    .. code-block:: py

        Block(11)

    data-types

    0-7: Level of the water, 0 being the highest, 7 the lowest


.. py:class:: SAND

    .. code-block:: py

        Block(12)


.. py:class:: GRAVEL

    .. code-block:: py

        Block(13)


.. py:class:: GOLD_ORE

    .. code-block:: py

        Block(14)


.. py:class:: IRON_ORE

    .. code-block:: py

        Block(15)


.. py:class:: COAL_ORE

    .. code-block:: py

        Block(16)


.. py:class:: WOOD

    .. code-block:: py

        Block(17)

    data-types (after 3 not on Pi)

    * **0** - Oak (up/down)
    * **1** - Spruce (up/down)
    * **2** - Birch (up/down)    
    * **3** - Jungle (up/down)
    * **4** - Oak (east/west)
    * **5** - Spruce (east/west)
    * **6** - Birch (east/west)
    * **7** - Jungle (east/west)
    * **8** - Oak (north/south)
    * **9** - Spruce (north/south)
    * **10** - Birch (north/south)
    * **11** - Jungle (north/south)
    * **12** - Oak (only bark)
    * **13** - Spruce (only bark)
    * **14** - Birch (only bark)
    * **15** - Jungle (only bark)


.. py:class:: LEAVES
    
    .. code-block:: py

        Block(18)

    data-types

    * **1** - Oak leaves
    * **2** - Spruce leaves
    * **3** - Birch leaves


.. py:class:: GLASS
    
    .. code-block:: py

        Block(20)


.. py:class:: LAPIS_LAZULI_ORE
    
    .. code-block:: py

        Block(21)


.. py:class:: LAPIS_LAZULI_BLOCK
    
    .. code-block:: py

        Block(22)


.. py:class:: SANDSTONE
    
    .. code-block:: py

        Block(24)

    data-types

    * **0** - Sandstone
    * **1** - Chiseled sandstone
    * **2** - Smooth sandstone


.. py:class:: BED
    
    .. code-block:: py

        Block(26)


.. py:class:: COBWEB
    
    .. code-block:: py

        Block(30)


.. py:class:: GRASS_TALL
    
    .. code-block:: py

        Block(31)

    data-types

    * **0** - Shrub
    * **1** - Grass
    * **2** - Fern
    * **3** - Grass (color affected by biome) (Not on Pi)


.. py:class:: WOOL
    
    .. code-block:: py

        Block(35)

    data-types

    * **0** - White
    * **1** - Orange
    * **2** - Magenta
    * **3** - Light Blue
    * **4** - Yellow
    * **5** - Lime
    * **6** - Pink
    * **7** - Grey
    * **8** - Light grey
    * **9** - Cyan
    * **10** - Purple
    * **11** - Blue
    * **12** - Brown
    * **13** - Green
    * **14** - Red
    * **15** - Black


.. py:class:: FLOWER_YELLOW
    
    .. code-block:: py

        Block(37)


.. py:class:: FLOWER_CYAN

    .. code-block:: py

        Block(38)


.. py:class:: MUSHROOM_BROWN

    .. code-block:: py

        Block(39)


.. py:class:: MUSHROOM_RED

    .. code-block:: py

        Block(40)


.. py:class:: GOLD_BLOCK

    .. code-block:: py

        Block(41)


.. py:class:: IRON_BLOCK

    .. code-block:: py

        Block(42)


.. py:class:: STONE_SLAB_DOUBLE

    .. code-block:: py

        Block(43)

    data-types

    * **0** - Stone
    * **1** - Sandstone
    * **2** - Wooden
    * **3** - Cobblestone
    * **4** - Brick
    * **5** - Stone Brick
    * **6** - Nether Brick (not on Pi)
    * **7** - Quartz (not on Pi)


.. py:class:: STONE_SLAB

    .. code-block:: py

        Block(44)

    data-types

    * **0** - Stone
    * **1** - Sandstone
    * **2** - Wooden
    * **3** - Cobblestone
    * **4** - Brick
    * **5** - Stone Brick
    * **6** - Nether Brick (not on Pi)
    * **7** - Quartz (not on Pi)


.. py:class:: BRICK_BLOCK

    .. code-block:: py

        Block(45)


.. py:class:: TNT

    .. code-block:: py

        Block(46)

    data-types

    * **0** - Inactive
    * **1** - Ready to explode


.. py:class:: BOOKSHELF

    .. code-block:: py

        Block(47)


.. py:class:: MOSS_STONE

    .. code-block:: py

        Block(48)


.. py:class:: OBSIDIAN

    .. code-block:: py

        Block(49)


.. py:class:: TORCH

    .. code-block:: py

        Block(50)

    data-types

    * **1**: Pointing east
    * **2**: Pointing west
    * **3**: Pointing south
    * **4**: Pointing north
    * **5**: Facing up


.. py:class:: FIRE

    .. code-block:: py

        Block(51)


.. py:class:: STAIRS_WOOD

    .. code-block:: py

        Block(53)

    data-types

    * **0** - Ascending east
    * **1** - Ascending west
    * **2** - Ascending south
    * **3** - Ascending north
    * **4** - Ascending east (upside down)
    * **5** - Ascending west (upside down)
    * **6** - Ascending south (upside down)
    * **7** - Ascending north (upside down)


.. py:class:: CHEST

    .. code-block:: py

        Block(54)

    data-types

    * **2** - Facing north
    * **3** - Facing south
    * **4** - Facing west
    * **5** - Facing east


.. py:class:: DIAMOND_ORE

    .. code-block:: py

        Block(56)


.. py:class:: DIAMOND_BLOCK

    .. code-block:: py

        Block(57)


.. py:class:: CRAFTING_TABLE

    .. code-block:: py

        Block(58)


.. py:class:: FARMLAND

    .. code-block:: py

        Block(60)


.. py:class:: FURNACE_INACTIVE

    .. code-block:: py

        Block(61)

    data-types

    * **2** - Facing north
    * **3** - Facing south
    * **4** - Facing west
    * **5** - Facing east


.. py:class:: FURNACE_ACTIVE

    .. code-block:: py

        Block(62)

    data-types

    * **2** - Facing north
    * **3** - Facing south
    * **4** - Facing west
    * **5** - Facing east


.. py:class:: DOOR_WOOD

    .. code-block:: py

        Block(64)


.. py:class:: LADDER

    .. code-block:: py

        Block(65)

    data-types

    * **2** - Facing north
    * **3** - Facing south
    * **4** - Facing west
    * **5** - Facing east


.. py:class:: STAIRS_COBBLESTONE

    .. code-block:: py

        Block(67)

    data-types

    * **0** - Ascending east
    * **1** - Ascending west
    * **2** - Ascending south
    * **3** - Ascending north
    * **4** - Ascending east (upside down)
    * **5** - Ascending west (upside down)
    * **6** - Ascending south (upside down)
    * **7** - Ascending north (upside down)


.. py:class:: DOOR_IRON

    .. code-block:: py

        Block(71)


.. py:class:: REDSTONE_ORE

    .. code-block:: py

        Block(73)


.. py:class:: SNOW

    .. code-block:: py

        Block(78)


.. py:class:: ICE

    .. code-block:: py

        Block(79)


.. py:class:: SNOW_BLOCK

    .. code-block:: py

        Block(80)

    data-types

    0-7: Height of snow, 0 being the lowest, 7 being the highest.


.. py:class:: CACTUS

    .. code-block:: py

        Block(81)


.. py:class:: CLAY

    .. code-block:: py

        Block(82)


.. py:class:: SUGAR_CANE

    .. code-block:: py

        Block(83)


.. py:class:: FENCE

    .. code-block:: py

        Block(85)


.. py:class:: GLOWSTONE_BLOCK

    .. code-block:: py

        Block(89)


.. py:class:: BEDROCK_INVISIBLE

    .. code-block:: py

        Block(95)


.. py:class:: STONE_BRICK

    .. code-block:: py

        Block(98)

    data-types
    
    * **0** - Stone brick
    * **1** - Mossy stone brick
    * **2** - Cracked stone brick
    * **3** - Chiseled stone brick


.. py:class:: GLASS_PANE

    .. code-block:: py

        Block(102)


.. py:class:: MELON

    .. code-block:: py

        Block(103)


.. py:class:: FENCE_GATE

    .. code-block:: py

        Block(107)

    data-types

    * **2** - Facing north
    * **3** - Facing south
    * **4** - Facing west
    * **5** - Facing east


.. py:class:: GLOWING_OBSIDIAN

    .. code-block:: py

        Block(246)


.. py:class:: NETHER_REACTOR_CORE

    .. code-block:: py

        Block(247)

    data-types

    * **0** - Unused
    * **1** - Active
    * **2** - Stopped / used up
