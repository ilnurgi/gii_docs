.. py:module:: kivy.uix.scrollview

scrollview
==========

ScrollView
----------

.. py:class:: ScrollView()

    Наследник :py:class:`kivy.uix.stencilview.StencilView`

    .. code-block:: py

        root = ScrollView(size_hint=(1, None))
        root.add_widget(layout)

    .. py:attribute:: always_overscroll
    .. py:attribute:: bar_color
    .. py:attribute:: bar_inactive_color
    .. py:attribute:: bar_margin
    .. py:attribute:: bar_pos
    .. py:attribute:: bar_pos_x
    .. py:attribute:: bar_pos_y
    .. py:attribute:: bar_width
    .. py:attribute:: do_scroll
    .. py:attribute:: do_scroll_x
    .. py:attribute:: do_scroll_y
    .. py:attribute:: effect_cls
    .. py:attribute:: effect_x
    .. py:attribute:: effect_y
    .. py:attribute:: hbar
    .. py:attribute:: scroll_distance
    .. py:attribute:: scroll_timeout
    .. py:attribute:: scroll_type

        * bars
        * content

        :py:class:`list`

    .. py:attribute:: scroll_wheel_distance
    .. py:attribute:: scroll_x
    .. py:attribute:: scroll_y
    .. py:attribute:: smooth_scroll_end
    .. py:attribute:: vbar
    .. py:attribute:: viewport_size

    .. py:method:: add_widget(widget, index=0)

    .. py:method:: convert_distance_to_scroll(dx, dy)
    .. py:method:: on_scroll_start()
    .. py:method:: on_scroll_move()
    .. py:method:: on_scroll_stop()

    .. py:method:: on_touch_down(touch)

        * touch - :py:class:`kivy.uix.input.motionevent.MotionEvent`

    .. py:method:: on_touch_move(touch)

        * touch - :py:class:`kivy.uix.input.motionevent.MotionEvent`

    .. py:method:: on_touch_up(touch)

        * touch - :py:class:`kivy.uix.input.motionevent.MotionEvent`

    .. py:method:: remove_widget(widget)

    .. py:method:: scroll_to(widget, padding=10, animate=True)
    .. py:method:: to_local(x, y, **k)
    .. py:method:: to_parent(x, y, **k)
    .. py:method:: update_from_scroll(*args)
