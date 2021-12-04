.. py:module:: kivy.graphics.instructions

canvas
======

Canvas
------

.. py:class:: Canvas()

    .. code-block:: py

        with self.canvas:
            Color(1, 1, 1, 1)
            Rectangle(
                pos=self.pos,
                size=self.size,
                source='download.png',
            )

    .. code-block:: py

        with self.canvas:
            Color(1, 1, 1, 1)
            self.rect = Rectangle()
            self.bind(
                pos=self.update_rect,
                size=self.update_rect,
            )

        def update_rect(self):
            self.rect.pos = self.pos
            self.rect.size = self.size