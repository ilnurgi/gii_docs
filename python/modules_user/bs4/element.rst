.. title:: python beautifulsoup element

.. meta::
    :description:
        Справочная информация по python модулю beautifulsoup.
        Модуль для обработки html структуры.
    :keywords:
        python beautifulsoup element

.. py:module:: beautifulsoup.element

element
=======

Tag()
-----

.. py:class:: Tag()

    Тег элемент


    .. py:attribute:: attrs

        Словарь атрибутов элемента

        .. code-block:: py

            table_elem.attrs
            # {'class': 'table'}

            image_elem.attrs['src']


    .. py:attribute:: children

        Список дочерних элементов :py:class:`Tag`

        .. code-block:: py

            for child in span_elem.children:
                print(child.get_text())


    .. py:attribute:: contents

    .. py:attribute:: descendants

        Список всех вложенных элементов :py:class:`Tag`

        .. code-block:: py

            for child in span_elem.descendants:
                print(child)


    .. py:attribute:: name

        Строка, название тега

        .. code-block:: py

            tag.name
            # 'a'


    .. py:attribute:: next_sibling

        Список всех элементов на уровне

        .. code-block:: py

            for sibling in table_elem.tr.next_sibling:
                print(sibling)


    .. py:attribute:: parent

        Родительский элемент :py:class:`Tag`

        .. code-block:: py

            table_elem.parent


    .. py:attribute:: previous_siblings

        Список всех элементов на уровне

        .. code-block:: py

            for sibling in table_elem.tr.previous_siblings:
                print(sibling)


    .. py:attribute:: string

        Текстовое содержимое тега, :py:class:`beautifulsoup.element.NavigableString`


    .. py:method:: text

        Текстовое содержимое


    .. py:method:: get_text()

        Возвращает только текст содержимого

        .. code-block:: py

            span_elem.get_text()
            # some text


    .. py:method:: find_all()

        Возвращает список всех найденных элементов


    .. py:method:: prettify()

        Возвращает текстовое содержимое

        .. code-block:: py

            span_elem.prettify()
            # <span>hello world</span>



NavigableString()
-----------------

.. py:class:: NavigableString()

    Текст внутри тегов


ResultSet()
-----------

.. py:class:: ResultSet()

    Список найденных эелементов