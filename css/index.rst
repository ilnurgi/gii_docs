.. title:: css

.. meta::
    :description: 
        Описание каскадных стилей описания веб документов.
    :keywords: 
        css

CSS
===

.. code-block:: html

    <link rel="stylesheet" href="main.css">
    <link rel="stylesheet" type="text/css" href="mysite.css">
    <link rel="stylesheet" type="text/css" href="http://www.mysite.ru/main.css">

    <style type="text/css">
        * {
            color: red;
        }
    </style>

.. code-block:: text
    
    :root {
        /* глобальная переменная */
        --color-red: red;
    }

    .wrapper {
        /* переменная элемента */
        --color-red: red;
        color: var(--color-red, blue);
    }


.. toctree::
    :maxdepth: 1

    selectors
    background
    border
    boxsizing
    clippath
    columncount
    font
    list
    marking
    table
    animation
    psevdoclass
    psevdoelements
    faq
    flex
    grid
    modules/index
    media


Цвета
-----

.. code-block:: css

    elem {
        color: red,
        color: #ff00ff,
        color: #f0f,
        color: rgb(255, 0, 255),
        color: rgb(100%, 0, 100%),
        color: rgba(255, 0, 255, 1),
        color: rgba(100%, 0, 100%, 1),

        /* тон, насыщенность, яркость */
        color: hsl(300, 100%, 50%),
        color: hsla(300, 100%, 50%, 1),

        /* голубой, пурпурный, желтый, черный */
        color: cmyk(29%, 55%, 0, 0),
    }


Единицы измерения
-----------------

* em - относительный, размера шрифта родительского элемента
* ex - относительный, высоты символа х в нижнем регистре
* ch - относительный, размера символа нуль
* rem - относительный, размера шрифта корневого элемента
* vw - относительный, ширины окна просмотра
* vh - относительный, высоты экрана просмотра
* vmin - наименьшее значение между vw и vh
* vmax - наибольшее значение между vw и vh
* px - относительный, разрешения экрана, 1/72 дюйма
* in - дюйм
* cm - сантиметры
* mm - милиметры
* pt - пункты, 1/72 дюйма
* pc - пика, 1/12 пункта
* % - относительный, родительского элемента
* dpi - разрешение точек на дюйм
* dpc - разрешение точек на сантиметр
* dppx - разрешение точек на пиксель

Угловые, временные и частоты

* deg - градусы
* grad - градиан, 1/400 окружности
* rad - радиан, 180/pi, ~57.3
* turn - оборот
* ms - миллисекунда
* s - секунда
* Hz - герц
* kHz - килогерц


content
-------

Текст, который появляется либо до, либо после элемента.

.. code-block:: css

    elem:before {
        content: "Before";
    }

    elem:after {
        content: "After";
    }


cursor
------

Определаяет форму указателя мышки

* auto - по умолчанию

* default

* crosshair

* pointer

* move

* e-resize

* ne-resize

* nw-resize

* resize

* se-resize

* sw-resize

* s-resize

* w-resize

* text

* wait

* help

* progress

.. code-block:: css

    elem {
        cursor: help;
    }

    elem1 {
        cursor: url(images/cursor.cur);
    }


linear-gradient
---------------

Градиентная заливка

.. code-block:: css

    elem {
        background: linear-gradient(top, #fff, #efefef);
    }


opacity
-------

Прозрачность элемента

.. code-block:: css

    elem {
        opacity: .5;
    }


.. _orphans:

orphans
-------

Минимальное количество строк текста, которые можно оставить внизу распечатанной страницы

.. code-block:: css

    elem {
        orphans: 3;
    }


page-break-after
----------------

Происходит ли разрыв страницы при печати после определенного элемента

* auto - по умолчанию

* always - элемент, который следует далее, появится вверху отдельной печатной страницы

* avoid - предотвращает обрыв страницы после элмента

* left

* right

.. code-block:: css

    elem {
        page-break-after: always;
    }


page-break-before
-----------------

Происходит ли разрыв страницы при печати перед определенным элементом

* auto - по умолчанию

* always - элемент, который следует перед, появится вверху отдельной печатной страницы

* avoid - предотвращает обрыв страницы перед элментом

* left

* right

.. code-block:: css

    elem {
        page-break-before: always;
    }


page-break-inside
-----------------

Препятствует тому, что элмент будет разбит на две печатные страницы

.. code-block:: css

    elem {
        page-break-inside: avoid;
    }


widows
------

Противоположное :ref:`orphans`, минимальное количество строк, которое должно появиться наверху печатной страницы

.. code-block:: css

    elem {
        widows: 5;
    }

filter
------

* blur()
* brightness()
* contrast()
* drop-shadow()
* grayscale()
* hue-rotate()
* invert()
* opacity()
* saturate()
* sepia()

.. code-block:: css

    .colorize-pink {
      filter: brightness(0.5) sepia(1) hue-rotate(-70deg) saturate(5);
    }

    .colorize-navy {
      filter: brightness(0.2) sepia(1) hue-rotate(180deg) saturate(5);
    }

    .colorize-blue {
      filter: brightness(0.5) sepia(1) hue-rotate(140deg) saturate(6);
    }