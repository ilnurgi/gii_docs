FormData
========

.. py:class:: FormData()

    тело HTTP-запроса multipart/form-data

    .. code-block:: js

        let form_data = new FormData()

    .. py:function:: append(string name, any value)
        
        До­бав­ля­ет в  объ­ект FormData но­вую часть с  име­нем name и зна­че­ни­ем value. 

        Ар­гу­мент value мо­жет быть стро­кой или объ­ек­том Blob.

        .. code-block:: js

            form_data.append('file', file)