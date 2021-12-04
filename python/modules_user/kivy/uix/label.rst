.. py:module:: kivy.uix.label

label
=====

Label
-----

.. py:class:: Label()

    .. code-block:: py

        Label(
            text='label',
            text='<b>label</b>',
            markup=True,
            font_size='20sp',
        )

    .. code-block:: text

        Label:
            size: self.texture.size
            text_size: cm(6), cm(4)
            text_size: root.width, None
            halign: 'right'
            valign: 'middle'
            font_size: 16
            markup: True
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size

    .. py:attribute:: color

        .. code-block:: text

            Label:
                color: 1, 0, 0, 0.5

    .. py:attribute:: font_size

    .. py:attribute:: halign

    .. py:atrribute:: pos

        .. code-block:: js

            Label:
                pos: 100, 200
                pos: '100dp', '200dp'

    .. py:atrribute:: size

        .. code-block:: js

            Label:
                size: 400, 200
                size: '400dp', '200dp'

    .. py:attribute:: text

        .. code-block:: text

            Label:
                text: 'Hello World'

    .. py:attribute:: text_size

        Размер области текста, который находится внутри Label

        .. code-block:: kv

            Label:
                # после этого valign, halign работают корректно
                text_size: self.size

    .. py:attribute:: valign

    .. warning:: дополнить
