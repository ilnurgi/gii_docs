.. title:: python gettext

.. meta::
    :description:
        Справочная информация по python модулю gettext.
    :keywords:
        python gettext

gettext
=======

Модуль для работы с локализацией

.. code-block:: text

    locales
    - en
    -- LC_MESSAGES
    --- myapp.mo
    --- myapp.po

.. code-block:: sh

    $ xgettext -o locales/en/LC_MESSAGES/myapp.po script.py
    # возможно данные по кодировке придется подправить в файле .po

    $ msgfmt locales/en/LC_MESSAGES/myapp.po -o locales/en/LC_MESSAGES/myapp.mo

install()
---------

.. py:function:: install(domain, localedir=None, codeset=None, names=None)

    Устанавливает функию _() в глобальное окружение скрипта

    .. code-block:: py

        gettext.install('myapp', 'locale')
        _('Hello')
        # привет


translation()
-------------

.. py:function:: translation(domain, localedir=None, languages=None, class_=None, fallback=False, codeset=None)

    Возвращает :py:class:`GNUTranslations`

    .. code-block:: py

        trans = gettext.translation('myapp', 'locales', ['en'])


GNUTranslations()
-----------------

.. py:class:: GNUTranslations()

    .. py:method:: gettext(message)

        .. code-block:: py

            trans.gettext('Привет')
            # Hello
