.. py:module:: kivy.uix.switch

switch
======

Switch
------

.. py:class:: Switch()

    .. py:class::`kivy.uix.widget.Widget`

    .. code-block:: py

        Switch(active=True)

    .. py:attribute:: active

        :py:class:`bool`

    .. py:attribute:: active_norm_pos

        :py:class:`bool`

    .. py:attribute:: touch_control

    .. py:attribute:: touch_distance

    .. py:method:: bind(**kwargs)

        * active

        .. code-block:: py

            Switch(active=True).bind(active=lambda instance, value: pass)

    .. py:method:: on_touch_down(touch)

        * touch - :py:class:`kivy.uix.input.motionevent.MotionEvent`

    .. py:method:: on_touch_move(touch)

        * touch - :py:class:`kivy.uix.input.motionevent.MotionEvent`

    .. py:method:: on_touch_up(touch)

        * touch - :py:class:`kivy.uix.input.motionevent.MotionEvent`
