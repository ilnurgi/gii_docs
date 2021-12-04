.. py:module:: kivy.uix.button

button
======

Button
------

.. py:class:: Button(**kwargs)

    .. code-block:: py

        Button(
            background_color=[1, 0, 0, 0],
            font_size=14,
            text='Button',
            on_press=callback,
        )

    .. code-block:: js

        Button:
            id: button
            text: 'button'
            on_press: print('on_press')
            on_press: root.say_hello()
            font_size: 30
            # font_size: '30sp'
            size_hint: (0.5, None)
            pos_hint: {'center_x': 0.5, 'top': 1}


    .. py:attribute:: background_color

        :py:class:`kivy.properties.ObservableList`

        .. code-block:: py

            btn.background_color
            # [1, 1, 1, 1]


    .. py:attribute:: background_disabled_down

        :py:class:`str`

        .. code-block:: py

            btn.background_disabled_down
            # atlas://data/images/defaulttheme/button_disabled_pressed


    .. py:attribute:: background_disabled_normal

        :py:class:`str`

        .. code-block:: py

            btn.background_disabled_normal
            # atlas://data/images/defaulttheme/button_disabled


    .. py:attribute:: background_down

        :py:class:`str`

        .. code-block:: py

            btn.background_down
            # atlas://data/images/defaulttheme/button_pressed


    .. py:attribute:: background_normal

        :py:class:`str`

        .. code-block:: py

            btn.background_normal
            # atlas://data/images/defaulttheme/button


    .. py:attribute:: border

        :py:class:`kivy.properties.ObservableList`

        .. code-block:: py

            btn.border
            # [16, 16, 16, 16]

    .. py:attribute:: color

        .. code-block:: text

            Button:
                color: 1, 0, 0, 0.5

    .. py:attribute:: font_size

        :py:class:`int`

    .. py:attribute:: on_press

    .. py:atrribute:: on_release

    .. py:atrribute:: on_state

    .. py:atrribute:: pos

        .. code-block:: js

            Button:
                pos: 100, 200
                pos: '100dp', '200dp'

    .. py:atrribute:: size

        .. code-block:: js

            Button:
                size: 400, 200
                size: '400dp', '200dp'

    .. py:atrribute:: size_hint

    .. py:atrribute:: size_hint_x

    .. py:atrribute:: size_hint_y

    .. py:attribute:: state

    .. py:attribute:: text

        :py:class:`str`

        .. code-block:: js

            Button:
                text: 'hello'

    .. py:atrribute:: width

    .. py:method:: bind(**kwargs)

        * on_press
        * on_release
        * on_state

        Связывает обработчик с кнопкой

        .. code-block:: py

            Button().bind(on_press=lambda instance: pass)
            Button().bind(on_state=lambda instance, value: pass)
