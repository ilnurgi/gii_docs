.. py:module:: kivy.config

config
======

Config
------

.. py:class:: Config()

    .. py:classmethod:: getint()

        .. code-block:: py

            Config.getint('kivy', 'show_fps')
            # 0


    .. py:classmethod:: set()

        .. code-block:: py

            Config.set('graphics', 'resizable', '0')
            Config.set('postproc', 'retain_time', '50')

    .. py:classmethod:: write()

        .. code-block:: py

            Config.set('graphics', 'resizable', '0')
            Config.write()

* kivy
    * default_font: list
    * desktop: int, 0 or 1
    * exit_on_escape: int, 0 or 1
    * pause_on_minimize: int, 0 or 1
    * keyboard_layout: string
    * keyboard_mode: string - включение режима экранной клавиатуры
        * ‘’ - Let Kivy choose the best option for your current platform.
        * ‘system’ - real keyboard.
        * ‘dock’ - one virtual keyboard docked to a screen side.
        * ‘multi’ - one virtual keyboard for every widget request.
        * ‘systemanddock’ - virtual docked keyboard plus input from real keyboard.
        * ‘systemandmulti’ - analogous.
    * kivy_clock: one of default, interrupt, free_all, free_only
    * log_dir: string
    * log_enable: int, 0 or 1
    * log_level: string, one of ‘trace’, ‘debug’, ‘info’, ‘warning’, ‘error’ or ‘critical’
    * log_name: string
    * log_maxfiles: int
    * window_icon: string
* postproc
    * double_tap_distance: float
    * double_tap_time: int
    * ignore: list of tuples
        * ignore = [(xmin, ymin, xmax, ymax), ...]
    * jitter_distance: int
    * jitter_ignore_devices: string, separated with commas
    * retain_distance: int
    * retain_time: int
    * triple_tap_distance: float
    * triple_tap_time: int
* graphics
    * borderless: int , one of 0 or 1
    * window_state: string , one of ‘visible’, ‘hidden’, ‘maximized’ or ‘minimized’
    * fbo: string, one of ‘hardware’, ‘software’ or ‘force-hardware’
    * fullscreen: int or string, one of 0, 1, ‘fake’ or ‘auto’
    * height: :py:class:`int`

        высота окна

        .. code-block:: py

            Config.set('graphics', 'height', 600)

    * left: int
    * maxfps: int, defaults to 60
    * multisamples: int, defaults to 2
    * position: string, one of ‘auto’ or ‘custom’
    * show_cursor: int, one of 0 or 1
    * top: int
    * resizable: :py:classL`int`, 0 или 1

        Возможность изменять размер окна приложения.

        .. code-block:: py

            Config.set('graphics', 'resizable', 0)
            Config.set('graphics', 'resizable', 1)


    * rotation: int, one of 0, 90, 180 or 270
    * width: :py:class:`int`

        ширина окна

        .. code-block:: py

            Config.set('graphics', 'width', 800)

    * minimum_width: int
    * minimum_height: int
    * min_state_time: float, defaults to .035
    * allow_screensaver: int, one of 0 or 1, defaults to 1
* input
* widgets
    * scroll_distance: int
    * scroll_friction: float
    * scroll_timeout: int
    * scroll_stoptime: int
    * scroll_moves: int
* modules

ConfigParser
------------

.. py:class:: ConfigParser(**kwargs)

    * name

    .. py:attribute:: name

    .. py:staticmethod:: get_configparser(name)

    .. py:method:: add_callback(callback, section=None, key=None)

        .. code-block:: py

            ConfigParser(name='kivy').add_callback(
                lambda section, key, value: pass
            )


    .. py:method:: adddefaultsection(section)

    .. py:method:: get(section, option, **kwargs)
    .. py:method:: getdefault(section, option, defaultvalue)
    .. py:method:: getdefaultint(section, option, defaultvalue)

    .. py:method:: remove_callback(callback, section=None, key=None)

    .. py:method:: set(section, option, value)
    .. py:method:: setall(section, keyvalues)
    .. py:method:: setdefault(section, option, value)
    .. py:method:: setdefaults(section, keyvalues)
    .. py:method:: updateconfig(filename, overwrite=None)
    .. py:method:: write()
