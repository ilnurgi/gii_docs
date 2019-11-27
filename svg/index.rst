.. title:: svg

.. meta::
    :description:
        Описание svg
    :keywords:
        svg

SVG
===

.. toctree::
    :maxdepth: 1

    circle
    ellipse

* class -
* height -
* fill - заливка
* fill-rule -
    * nonzero -
    * evenodd -
    * inherit -
* preserveAspectRatio -
* stroke - обводка
* stroke-dasharray - вид пунктирной обводки
* stroke-dashoffset - смещениепунктирной обводки
* stroke-linecap -
    * butt cap -
    * round cap -
    * square cap -
* stroke-linejoin -
    * miter join -
    * round join -
    * bevel join -
* viewBox -
* width -



.. code-block:: xml

    <svg
        width="500"
        height="200"
        class="brd"
        viewBox="0 0 200 200"
    >
      <!--svg code-->
    </svg>


defs
----

Элемент не отображается на холсте, но будет отображаться если на неё сослаться через xlink:href.

g
-

Контейнер для группировки связанных графических элементов

* id -

.. code-block:: xml

    <g id="my_group">
        <!--svg-->
        <!--svg-->
        <!--svg-->
    </g>


line
----

.. code-block:: xml

    <line
        x1="10"
        y1="10"
        x2="200"
        y2="200"
        style="stroke:rgb(255,0,0);stroke-width:2"
        />


linearGradient
--------------

.. code-block:: xml

    <linearGradient
        id="Gradient1"
        x1="0"
        y1="0"
        x2="0"
        y2="100%"
    >
        <stop
            offset="0%"
            stop-color="#00F"
            />
        <stop
            offset="100%"
            stop-color="#0F0"
            />
    </linearGradient>


path
----

Путь


polygon
-------

.. code-block:: xml

    <polygon
        points="300,10 350,140 60,200 100,100"
        style="fill:#408528;stroke:#286E85;stroke-width:3;fill-rule:evenodd"
        />


polyline
--------

.. code-block:: xml

    <polyline
        points="210,40 40,40 40,30 30,80 80,120 120,120 170,190"
        fill="white"
        fill-rule="inherit"
        stroke="#853F28"
        stroke-width="6"
        />


rect
----

.. code-block:: xml

    <rect
        x="50"
        y="20"
        width="150"
        height="150"
        class="svg-rect"
        />
    <rect
        x="250"
        y="20"
        rx="40"
        ry="40"
        width="150"
        height="150"
        class="svg-rect"
        style="fill-opacity:1;stroke-opacity:1;"
        fill="url(#Gradient1)"
        stroke="#333333"
        stroke-width="4px"
        />


symbols
-------

Группирует элементы, но не отображает их, но будет отображаться если на неё сослаться через xlink:href.


text
----

.. code-block:: xml

    <text
        x="20"
        y="120"
        fill="#ED6E46"
        font-size="100"
        font-family="'Arial', cursive"
    >
        ilnurgi1.ru
    </text>


use
---

.. code-block:: xml

    <g id="my_group">
        <!--svg-->
        <!--svg-->
        <!--svg-->
    </g>
    <use
        x="50"
        y="50"
        xlink:href="my_group"
        />