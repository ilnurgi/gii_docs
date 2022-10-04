.. py:module:: kivy.uix.scrollview

scrollview
==========

ScrollView
----------

.. py:class:: ScrollView()

    Наследник :py:class:`kivy.uix.stencilview.StencilView`

    Скроллируемый виджет. Содержит только 1 виджет.

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

        По умолчанию - True, разрешен скролл по оси Х.

    .. py:attribute:: do_scroll_y

        По умолчанию - True, разрешен скролл по оси У.

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

        Принимает 0 или 1. 
        * 0 - скролл вниз
        * 1 - скролл вверх

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


FAQ
---

Скроллируемый текстовый просмотрщик
+++++++++++++++++++++++++++++++++++


.. code-block:: py

    def build(self):
        
        self.label = Label(
            size_hint_y=None,
            size_hint_x=None,
        )

        self.scroll_view = ScrollView()
        self.scroll_view.add_widget(self.label)

    def append_text_label(self, text):

        self.label.text = f'{self.label.text}\n{text}'

        # обновляем сведения по текстуре виджета
        self.label.texture_update()
        # задаем размер виджета по текстуре
        self.label.size = self.label.texture_size

        # скролим виджет до конца вниз
        self.scroll_view.scroll_y = 0


