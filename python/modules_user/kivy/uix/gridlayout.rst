.. py:module:: kivy.uix.gridlayout

gridlayout
==========

GridLayout
----------

.. py:class:: GridLayout(**kwargs)

    Наследник :py:class:`kivy.uix.layout.Layout`

    .. code-block:: py

        GridLayout(
            cols=3,
            row_force_default=True,
            row_default_height=40,
            padding=[left, top, right, bottom],
        )

    .. code-block:: py

        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

    .. py:attribute:: col_default_width
    .. py:attribute:: col_force_default
    .. py:attribute:: cols

        :py:class:`int`

    .. py:attribute:: cols_minimum
    .. py:attribute:: minimum_height
    .. py:attribute:: minimum_size
    .. py:attribute:: minimum_width
    .. py:attribute:: orientation

         ‘lr-tb’, ‘tb-lr’, ‘rl-tb’, ‘tb-rl’, ‘lr-bt’, ‘bt-lr’, ‘rl-bt’ and ‘bt-rl’.

    .. py:attribute:: orientation
    .. py:attribute:: padding
    .. py:attribute:: row_default_height
    .. py:attribute:: row_force_default
    .. py:attribute:: rows
    .. py:attribute:: rows_minimum

    .. py:attribute:: size_hint_y

    .. py:attribute:: spacing

        :py:class:`int`

    .. py:method:: do_layout(*args)
