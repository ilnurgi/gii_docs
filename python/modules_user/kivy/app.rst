.. py:module:: kivy.app

app
===

App
---

.. py:class:: App()

    .. code-block:: py

        class MyApp(App):
            """"""

        MyApp().run()

    .. py:attribute:: title

        :py:class:`str`

    .. py:method:: build()

        Возвращает виджеты окна

        .. code-block:: py

            def build(self):
                return Button()
