.. py:module:: markdown

markdown
========

Markdown_

`Официальная документация`_

.. code-block:: sh

    $ pip install markdown


.. code-block:: py
    
    import markdown


markdown()
----------

.. py:function:: markdown(text, **kwargs)

    Преобразует текст

    * extensions - список, расширения

    * extensions_config - словарь, конфигурирование расширений 

    * output_format - строка, формат возвразаемых данных

        * xhtml - по умолчанию
        * html5

    * tab_length - размер табуляции, по умолчанию 4

    .. code-block:: py

        markdown.markdown('# hello world')
        # <h1>hello world</h1>


markdownFromFile()
------------------

.. py:function:: markdownFromFile(**kwargs)

    Работает аналогично, как и :py:meth:`markdown.markdown()`, только данные берет из файла

    * input - обязательный, источник

        * путь к файлу
        * файло подобный объект
        * None, чтение из stdin

    * output - выходной объект

        * путь к файлу
        * файло подобный объект
        * None, чтение из stdin

    * encoding - кодировка, по умолчанию utf-8


Markdown()
----------

.. py:class:: Markdown()

    .. code-block:: py

        md = Markdown()

    .. py:method:: convert(source)

        Преобразует текст

        .. code-block:: py

            html = md.convert(text)

    .. py:method:: convertFile(**kwargs)

    .. py:method:: reset()

.. _Markdown: https://daringfireball.net/projects/markdown/
.. _Официальная документация: https://python-markdown.github.io/