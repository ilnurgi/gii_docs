.. py:module:: kivy.graphics

graphics
========

.. toctree::
    :maxdepth: 1

    instructions/index
    transformation


Color
-----

.. py:class:: Color(r, g, b, a)

    .. code-block:: py

        Color(0, 1, 0, 1)


Ellipse
-------

.. py:class:: Ellipse()

    .. code-block:: py

        Ellipse(pos=(100, 100), size=(50, 50))


Line
----

.. py:class:: Line()

    .. code-block:: py

        Line(
            points=(100, 100, 150, 200, 200, 100),
            close=True,
            width=5,
            joint='none',  # round, bevel, miter
            cap='square',  # round
        )


Rectangle
---------

.. py:class:: Rectangle()

    .. code-block:: py

        Rectangle(
            pos=(100, 100),
            size=(50, 50),
            source='download.png',
        )