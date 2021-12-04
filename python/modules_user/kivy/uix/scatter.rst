.. py:module:: kivy.uix.scatter


scatter
=======

Scatter
-------

.. py:class:: Scatter(**kwargs)

    * do_rotation - :py:class:`bool`
    * do_scale - :py:class:`bool`
    * do_translation_y - :py:class:`bool`
    * scale_min - :py:class:`float`
    * scale_max - :py:class:`float`

    Наследник :py:class:`kivy.uix.widget.Widget`

    .. code-block:: py

        scatter = Scatter()
        scatter.add_widget(Button())
        Scatter(scale_min=0.5, scale_max=3)

    .. py:attribute:: auto_bring_to_front

    .. py:attribute:: bbox

    .. py:attribute:: do_collide_after_children

    .. py:attribute:: do_rotation

    .. py:attribute:: do_scale

    .. py:attribute:: do_translation

    .. py:attribute:: do_translation_x

    .. py:attribute:: do_translation_y

    .. py:method:: add_widget(widget)

    .. py:method:: apply_transform(trans, post_multiply=False, anchor=(0, 0))

        * trans: :py:class:`kivy.graphics.transformation.Matrix`

        .. code-block:: py

            scatter.apply_transform(Matrix().scale(3, 3, 3))

    .. py:method:: collide_point(x, y)

    .. py:method:: on_bring_to_front()

    .. py:method:: on_transform_with_touch()

    .. warning:: дополнить
