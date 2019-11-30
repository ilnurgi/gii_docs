.. title:: css media

.. meta::
    :description:
        Описание css элемента media.
    :keywords:
        css media

media
=====

all
---

Все устройства


braille
-------

Устройства с тактильной обратной связью


embossed
--------

Брайлевсике принтеры


handled
--------

Портативные устройства


print
-----

Принтеры


projection
----------

Проекторы


screen
------

Цветные экраны


speech
------

Речевые синтезаторы


tty
---

Моноширинная символьная среда


tv
--

aspect-ratio()
--------------

Соотношение сторон области просмотра

.. code-block:: css

    @media (aspect-ratio: 16/9) {}


color()
-------

Количество бит на цвет


color-index()
-------------

Количесвто записей в таблице подстановки цветов

device-aspect-ratio()
---------------------

Соотношение сторон экрана


device-width()
--------------
device-height()
---------------

Ширина, высота экрана


grid()
------

Устройство с фиксированным размером символов


height()
--------

Высота области просмотра


hover()
-------

pointer()
---------


min-aspect-ratio()
------------------
max-aspect-ratio()
------------------

Минимальное, максимальное соотношение сторон

min-device-aspect-ratio()
-------------------------
max-device-aspect-ratio()
-------------------------

min-device-height()
-------------------
max-device-height()
-------------------

min-device-width()
------------------
max-device-width()
------------------


min-height()
------------
max-height()
------------
min-width()
-----------
max-width()
-----------

.. code-block:: css

    @media screen and (max-width: 960px){}

    /* Desktops 1281px или больше */
    @media (min-width: 1281px) {}

    /* Laptops, Desktops между 1025px и 1280px */
    @media (min-width: 1025px) and (max-width: 1280px) {}

    /* Tablets, Ipads (portrait) между 768px и 1024px */
    @media (min-width: 768px) and (max-width: 1024px) {}

    /* Tablets, Ipads (landscape) между 768px и 1024px */
    @media (min-width: 768px) and (max-width: 1024px) and (orientation: landscape) {}

    /* Low Resolution Tablets, Mobiles (Landscape) между 481px и 767px */
    @media (min-width: 481px) and (max-width: 767px) {}

    /* Most of the Smartphones Mobiles (Portrait) между 320px и 479px */
    @media (min-width: 320px) and (max-width: 480px) {}


monochrome()
------------

Сколько бит на каждый пиксель


orientation()
-------------

Ориентация экрана

* **landscape** - альбом, ширина области видимости больше высоты
* **portrait** - портрет, высота области видимости больше ширины

.. code-block:: css

    @media screen and (orientation: landscape) {}

resolution()
------------

Разрешение экрана или печати


scan()
------

Тип развертки

width()
-------

Ширина области просмотра
