.. py:module:: kivy

kivy
=====

https://kivy.org/

.. toctree::
    :maxdepth: 1

    app
    builder
    config
    core
    graphics/index
    input/index
    properties/index
    uix/index
    utils

.. toctree::
    :maxdepth: 1

    kv


.. code-block:: py

    from kivy.app import App
    from kivy.uix.label import Label

    class MyApp(App):

        def build(self):
            return Label(text='Hello World!')

    MyApp().run()
