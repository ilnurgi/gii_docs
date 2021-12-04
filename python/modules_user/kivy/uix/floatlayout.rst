.. py:module:: kivy.uix.floatlayout

floatlayout
===========

FloatLayout
-----------

.. py:class:: FloatLayout(**kwargs)

    * size - :py:class:`tuple`

    Наследник :py:class:`kivy.uix.layout.Layout`

    .. code-block:: py

        float_layout = FloatLayout(
            size=(300, 300),
        )
        float_layout.add_widget(Button(text='button'))
        float_layout.add_widget(
            Button(
                text='button',
                size_hint=(0.5, 0.25),
                pos=(20, 20),
            )
        )
        float_layout.add_widget(
            Button(
                text='button',
                size_hint=(0.5, 0.25),
                pos_hint={
                    'x': 0.2,
                    'y': 2,
                },
            )
        )

    .. py:method:: add_widget(widget, index=0, canvas=None)

    .. py:method:: do_layout(*args, **kwargs)

    .. py:method:: remove_widget(widget)