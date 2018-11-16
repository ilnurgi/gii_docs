HTMLTableElement
================

.. py:class:: HTMLTableElement

    Элемент `<table>`

    Наследник :py:class:`HTMLElement`

    .. code-block:: js

        let table_elem = document.querySelector('table');


    .. py:attribute:: border

    .. py:attribute:: caption

    .. py:attribute:: cellPadding

    .. py:attribute:: cellSpacing

    .. py:attribute:: rows[]

    .. py:attribute:: summary

    .. py:attribute:: tBodies[]

    .. py:attribute:: tFoot

    .. py:attribute:: tHead

    .. py:attribute:: width

    .. py:function:: createCaption()

    .. py:function:: createTFoot()

    .. py:function:: createTHead()

        Создает зоголовок и возвращает :py:class:`HTMLTableSectionElement`

        .. code-block:: js

            let thead_elem = table_elem.createTHead()


    .. py:function:: deleteCaption()

    .. py:function:: deleteTFoot()

    .. py:function:: deleteTHead()

    .. py:function:: deleteRow(index)

    .. py:function:: insertRow(index)