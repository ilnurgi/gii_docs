.. py:module:: kivy.uix.widget

widget
======

Widget
------

.. py:class:: Widget()

    .. code-block:: py

        class PainterWidget(Widget):

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

                with self.canvas:
                    Color(0, 1, 0, 1)
                    Ellipse(pos=(100, 100), size=(50, 50))

    .. py:attribute:: children

        :py:class:`list`

    .. py:method:: export_to_png()
    .. py:method:: on_touch_down(touch)
    .. py:method:: on_touch_move(touch)

    .. py:method:: walk(restrict=False, loopback=False)

        .. code-block:: kivy

            GridLayout:
                Button
                BoxLayout:
                    id: box
                    Widget
                    Button
                Widget

        .. code-block:: py

            [type(widget) for widget in box.walk(loopback=True)]
            # [<class 'BoxLayout'>, <class 'Widget'>, <class 'Button'>,
            #    <class 'Widget'>, <class 'GridLayout'>, <class 'Button'>]

            [type(widget) for widget in box.walk()]
            # [<class 'BoxLayout'>, <class 'Widget'>, <class 'Button'>,
            #    <class 'Widget'>]

            [type(widget) for widget in box.walk(restrict=True)]
            # [<class 'BoxLayout'>, <class 'Widget'>, <class 'Button'>]

    .. py:method:: walk_reverse(loopback=False)

        .. code-block:: kv

            GridLayout:
                Button
                BoxLayout:
                    id: box
                    Widget
                    Button
                Widget

        .. code-block:: py

            [type(widget) for widget in box.walk_reverse(loopback=True)]
            # [<class 'Button'>, <class 'GridLayout'>, <class 'Widget'>,
            #    <class 'Button'>, <class 'Widget'>, <class 'BoxLayout'>]

            [type(widget) for widget in box.walk_reverse()]
            # [<class 'Button'>, <class 'GridLayout'>]
