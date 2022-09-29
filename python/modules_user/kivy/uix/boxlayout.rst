.. py:module:: kivy.uix.boxlayout

boxlayout
=========

BoxLayout
---------

.. py:class:: BoxLayout(**kwargs)

    .. code-block:: py

        BoxLayout(
            orientation='vertical',
            padding=[left, top, right, bottom],
            padding=[all],
            padding=[left-right, top-bottom],
            spacing=100,
        )

    .. code-block:: js

        BoxLayout:
            orientation: 'vertical'
            padding: 20
            spacing: 20
            Label:
                text: 'label'


    .. py:attribute:: height

        Высота виджета

        .. code-block:: py

            BoxLayout(
                height=100,
                # иначе высота не применится
                size_hint_y=None,
            )


    .. py:attribute:: minimum_height
    .. py:attribute:: minimum_size
    .. py:attribute:: minimum_width
    .. py:attribute:: orientation

        * horizontal
        * vertical

        :py:class:`str`

        .. code-block:: py

            BoxLayout(
                orientation='vertical'
            )

    .. py:attribute:: padding

        :py:class:`int`

        Внутренний отступ

        .. code-block:: py

            BoxLayout(
                padding=10,
            )

    .. py:attribute:: spacing

        :py:class:`int`

    .. py:method:: add_widget(widget, index=0, canvas=None)

        .. code-block:: py

            BoxLayout().add_widget(Button())

    .. py:method:: do_layout(*args)

    .. py:method:: remove_widget(widget)
