.. py:module:: kivy.uix

uix
===

Виджеты:
--------

.. toctree::
    :maxdepth: 1

    button
    camera
    carousel
    checkbox
    dropdown
    image
    label
    modalview
    scatter
    stencilview
    switch
    textinput
    togglebutton
    widget


Лэйауты
-------

.. toctree::
    :maxdepth: 1

    anchorlayout
    layout
    boxlayout
    floatlayout
    gridlayout
    pagelayout
    screenmanager

FAQ
---

Рамка вокруг виджета/лэйаута
++++++++++++++++++++++++++++

.. code-block:: py

    class BorderedBoxLayout(BoxLayout):
        """BoxLayout с рамкой
        """

        def on_size(self, instance, value):
            """каллбак изменения размера лэйаута
            """
            with self.canvas:
                Color(1, 0, 0, 1)
                Line(
                    width=2,
                    rectangle=(self.x, self.y, self.width, self.height)
                )
