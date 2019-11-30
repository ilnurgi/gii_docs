.. title:: python webbrowser

.. meta::
    :description: 
        Справочная информация по модулю webbrowser, написанного для python.    
    :keywords: 
        python,
        python webbrowser

.. py:module:: webbrowser

webbrowser
==========

.. code-block:: sh

    python -m webbrowser -t "ilnurgi.ru"


get()
-----

.. py:function:: get(using=None)

    Возвращает объект браузера

    .. code-block:: py

        webbrowser.get().open_new_tab('ilnurgi.ru')
        webbrowser.get('google-chrome').open_new_tab('ilnurgi.ru')


open()
------

.. py:function:: open(url, new=0, autoraise=True)

    Открывает ссылку в браузере по умолчанию.

    * new 

        * 0 - ссылка открывается в том же окне браузера
        * 1 - ссылка открывается в новом окне браузера
        * 2 - ссылка открывается в новой вкладке

    .. code-block:: py

        webbrowser.open('http://ilnurgi.ru')


open_new()
----------

.. py:function:: open_new(url)

    Открывает ссылку в браузере по умолчанию.

    .. code-block:: py

        webbrowser.open_new('http://ilnurgi.ru')


open_new_tab()
--------------

.. py:function:: open_new_tab(url)

    Открывает ссылку в браузере по умолчанию.

    .. code-block:: py

        webbrowser.open_new_tab('http://ilnurgi.ru')


register()
----------

.. py:function:: register(name, constructor, instance=None, *, preferred=False)

    Регистрирует броузер

    * mozilla - Mozilla('mozilla')
    * firefox - Mozilla('mozilla')
    * netscape - Mozilla('netscape')
    * galeon - Galeon('galeon')
    * epiphany - Galeon('epiphany')
    * skipstone - BackgroundBrowser('skipstone')
    * kfmclient - Konqueror()
    * konqueror - Konqueror()
    * kfm - Konqueror()
    * mosaic - BackgroundBrowser('mosaic')
    * opera - Opera()
    * grail - Grail()
    * links - GenericBrowser('links')
    * elinks - Elinks('elinks')
    * lynx - GenericBrowser('lynx')
    * w3m - GenericBrowser('w3m')
    * windows-default - WindowsDefault
    * macosx - MacOSX('default')
    * safari - MacOSX('safari')
    * google-chrome - Chrome('google-chrome')
    * chrome - Chrome('chrome')
    * chromium - Chromium('chromium')
    * chromium-browser - Chromium('chromium-browser')

    .. code-block:: py

        webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('chrome.exe'))
        webbrowser.get('Chrome').open_new_tab('ilnurgi.ru')


BackgroundBrowser()
-------------------

.. py:class:: BackgroundBrowser()


Error()
-------

.. py:class:: Error()