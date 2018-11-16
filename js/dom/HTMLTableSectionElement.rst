HTMLTableSectionElement
=======================

.. py:class:: HTMLTableSectionElement

	Элемент `<tbody>`, `<tfoot>`, `<thead>`

	Наследник :py:class:`HTMLElement`

	.. code-block:: js

	    let thead_elem = table_elem.createTHead()
    

    .. py:attribute:: align

    .. py:attribute:: rows

    .. py:attribute:: vAlign

    .. py:function:: deleteRow(index)

    .. py:function:: insertRow([index])

    	Вставляет новую строку и возвращает :py:class:`HTMLTableRowElement`

    	.. code-block:: js

    		let tabel_row = thead_elem.insertRow()
