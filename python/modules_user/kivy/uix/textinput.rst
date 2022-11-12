.. py:module:: kivy.uix.textinput

textinput
=========

TextInput
---------

.. py:class:: TextInput(**kwargs)

    Наследник :py:class:`kivy.uix.behaviors.focus.FocusBehavior`, :py:class:`kivy.uix.widget.Widget`

    .. code-block:: py

        TextInput(
            text='Hello world',
            multiline=False,
        )

    .. code-block:: py

        TextInput:
            multiline: True
            size_hint: (0.5, None)
            pos_hint: {'center': 0.5, 'top': 1}
            height: 50
            font_size: 30

    .. py:attribute:: allow_copy
    .. py:attribute:: auto_indent
    .. py:attribute:: background_active
    .. py:attribute:: background_color

        :py:class:`list`

    .. py:attribute:: background_disabled_normal
    .. py:attribute:: background_normal
    .. py:attribute:: background_direction
    .. py:attribute:: border
    .. py:attribute:: focus

        :py:class:`bool`

    .. py:attribute:: font_size

    .. py:attribute::input_filter

        * 'int'

    .. py:attribute:: input_type

        * 'number'

    .. py:attribute:: multiline

        :py:class:`bool`

    .. py:attribute:: readonly

        :py:class:`bool`, возможность редактирования текста

    .. py:attribute:: text

        :py:class:`str`

    .. py:attribute:: size_hint

        :py:class:`list`

    .. py:method:: bind()

        .. code-block:: py

            def on_text(instance, value):
                """"""

            TextInput().bind(text=on_text)
            TextInput().bind(focus=on_focus)

    .. py:method:: insert_text(substring, from_undo=False)

    .. py:method:: on_double_tap()
    .. py:method:: on_text_validate()
    .. py:method:: on_triple_tap()
    .. py:method:: on_quad_touch()

    .. warning:: дополнить