.. title:: css transform

.. meta::
    :description:
        Описание css стиля transform.
    :keywords:
        css transform

transform
=========

Трансформация объектов

.. code-block:: css

    .class {
        transform: skew(45deg 0) rotate(200deg) translate(100px, 0) scale(.5);
    }


perspective()
-------------

rotate()
--------

rotateX()
---------

rotateY()
---------

rotate3d()
----------

.. code-block:: css

    .class {
        transform: rotate(10deg);
    }


scale()
-------

scaleX()
--------

scaleY()
--------

scale3d()
---------

.. code-block:: css

    .class {
        transform: scale(2);
    }


skew()
------

skewX()
-------

skewY()
-------

.. code-block:: css

    .class {
        transform: skew(-10deg);
    }


translate()
-----------

translateX()
------------

translateY()
------------

translate3d()
-------------

.. code-block:: css

    .class {
        transform: translateY(100px);
        transform: translate(-2rem, 100%);
    }
