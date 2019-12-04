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
any-hover()
-----------

Функция позволяет браузеру узнать,
может ли основной механизм ввода наводиться на элементы
(например, как курсор мыши).

* **hover** - может наводиться на элементы

* **none** - не может наводиться на элементы или механизма ввода с возможностью наведения нет вообще

.. code-block:: css

    @media screen and (hover: hover) {}


inverted-colors()
-----------------

* **inverted** - применить стили, если цвета инвертированы
* **none** - применить стили по умолчанию

.. code-block:: css

    @media screen and (inverted-colors: inverted) {}


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


pointer()
---------
any-pointer()
-------------

Функции позволяют браузеру узнать,
имеет ли основной механизм ввода указатель (например, мышь) и если имеет,
то насколько он точный.

* **coarse** - включает в себя указательно ограниченной точности

* **fine** - включает в себя точное указатель

* **none** - не включает в себя указатель


prefers-color-scheme()
----------------------

Предпочтительная цветовая схема

* **light** -  применить стили, если пользователь предпочитает светлую тему
* **dark** -  применить стили, если пользователь предпочитает тёмную тему
* **no-preference** - применить стили по умолчанию

.. code-block:: css

    @media screen and (prefers-color-scheme: dark) {}


prefers-reduced-motion()
------------------------

Сокращение количества анимации

* **reduce** - применяет стили, если пользователь не хочет видеть анимации и переходы

* **no-preference** - применяет обычные стили

.. code-block:: css

    @media screen and (prefers-reduced-motion: reduce) {}


resolution()
------------

Разрешение экрана или печати


scan()
------

Тип развертки

width()
-------

Ширина области просмотра
