Псевдоклассы
============

active
------

Текущий активный элемент

.. code-block:: css

    a:active {}


after
-----

Вставка контента после элемента

.. code-block:: css

    p:after {
        content: "...";
    }


checked
-------

Выбранный флажок

.. code-block:: css

    input[type=checkbox]:checked {}


default
-------


disabled
--------

Элемент формы - отключенный

.. code-block:: css

    input:disabled {}


empty
-----

Элемент не имеющий дочерних элементов


enabled
-------

Доступный элемент

.. code-block:: css

    input:enabled {}


first-child
-----------

Поиск первого дочернего элемента

.. code-block:: css

    p:first-child{}


first-of-type
-------------

Поиск первого элемента заданного типа на том же уровне

.. code-block:: css

    p:first-of-type {}


focus
-----

Элемент в фокусе

.. code-block:: css

    input:focus {}


focus-within
------------

Дочерний элемент в фокусе

.. code-block:: css

    form:focus-within {}


hover
-----

Элемент над которым находится мышка

.. code-block:: css

    input:hover {}


in-range
--------

Элементы имеющие ограничения диапазона значений, значения которых не выходят за рамки


indeterminate
-------------

Элемент формы в неопределенном состоянии

.. code-block:: css

    input:indeterminate {}


invalid
-------

Элемент формы не валидный

.. code-block:: css

    input:invalid {}


last-child
----------

Поиск последнего дочернего элемента

.. code-block:: css

    p:last-child {}


last-of-type
------------

Поиск последнего элемента заданного типа на том же уровне

.. code-block:: css

    p:last-of-type{}


lang
----

Элемент указанного языка

.. code-block:: css

    p:lang(en)


link
----

Не посещенная ссылка

.. code-block:: css

    a:link {}


not
---

Отрицание

.. code-block:: css

    input[type="checkbox"]:not(:checked)

.. code-block:: css

    input:not([type=submit]) {}


nth-child
---------

Поиск заданного дочернего элемента в прямом направлении

* even - все четные элементы

* odd - все нечетные элементы

* число - порядковый номер элемента, от 1

* выражение - вида an + b

.. code-block:: css

    p:nth-child(2n+1){}
    p:nth-child(odd){}
    p:nth-child(even){}
    p:nth-child(2){}


nth-last-child
--------------

Поиск заданного дочернего элемента в обратном напрвлении

.. code-block:: css

    p:nth-last-child(2) {}


nth-last-of-type
----------------

Поиск элементов типа на том же уровне в обратном направлений


nth-of-type
-----------

Поиск элементов типа на том же уровне

.. code-block:: css

    p:nth-of-type(2n+1) {}
    p:nth-of-type(even) {}
    p:nth-of-type(odd) {}


only-child
----------

Единственный дочерний элемент


only-of-type
------------

Единственный элемент этого типа на одном уровне


out-range
---------

Элементы имеющие ограничения диапазона значений, значения которых выходят за рамки


read-only
---------

Элементы только для чтения


read-write
----------

Элементы которые пользователь может редактировать


required
--------

Элементы форм с обязательным атрибутом

.. code-block:: css

    input:required {}


root
----

Корневой элемент, html


target
------

Элемент является текущей целью документа


valid
-----

Валидный элемент формы

.. code-block:: css

    input:valid {}


visited
-------

Посещенная ссылка

.. code-block:: css

    a:visited {}

