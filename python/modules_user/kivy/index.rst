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


Разработка под android
----------------------

.. code-block:: sh

    # ubuntu 
    $ python3 get-pip.py
    $ sudo apt-get install python3-venv
    $ python3 -m venv venv
    $ python -m pip install "kivy[base]" kivy_examples cython

    # buildozer
    $ sudo apt-get install zlib1g-dev openjdk-18-jre openjdk-18-jdk build-essential autoconf automake libltdl-dev libffi-dev libssl-dev
    $ git clone https://github.com/kivy/buildozer.git
    $ cd buildozer
    $ python setup.py install
    $ cd app_dir
    $ buildozer init
    $ buildozer android debug

