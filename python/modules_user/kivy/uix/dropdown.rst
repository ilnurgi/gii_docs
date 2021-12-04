.. py:module:: kivy.uix.dropdown

dropdown
========

DropDown
--------

.. py:class:: DropDown()

    .. code-block:: py

        drop_down = DropDown()
        drop_down.add_widget(
            Button(
                text=text,
                size_hint_y=None,
                height=40,
                on_release=lambda btn: drop_down.select(btn.text),
            )
        )
        main_btn = Button(
            text=text,
            on_release=drop_down.open,
        )
        drop_down.bind(
            on_select=lambda instance, value: main_btn.text=value,
        )

    .. py:method:: add_widget(widget)