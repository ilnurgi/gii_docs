DOMTokenList 
============


.. py:class:: DOMTokenList()
    
    Множество лексем, разделенных пробелами


    .. py:attribute:: length
    
        Ко­ли­че­ст­во уни­каль­ных лек­сем, со­дер­жа­щих­ся в нем.

    .. py:attribute:: value

        Список объектов :py:class:`DOMString`

    .. py:function:: add(string token)

        Если :py:class:`DOMTokenList` еще не содержит лексему token,
        она будет добавлена в конец списка.
    

    .. py:function:: contains(string token)
        
        Возвращает true, если объект :py:class:`DOMTokenList` содержит лексему token,
        или false – в противном случае.


    .. py:function:: item(unsigned long index)
    
        Воз­вра­ща­ет лек­се­му по ука­зан­но­му ин­дек­су или null, ес­ли ин­декс index вы­хо­дит за гра­ни­цы мас­си­ва. Объ­ект DOMTokenList мож­но так­же ин­дек­си­ро­вать не­по­сред­ст­ вен­но, не при­бе­гая к это­му ме­то­ду.


    .. py:function:: remove(string token)
    
        Удаляет указанную лексему.


    .. py:function:: toggle(string token[, bool force])
    
        Добавляет/удаляет `token` из объекта.

        Возвращает результат операции, true - если объект есть после вызова, иначе false

        Если `force` false - `token` будет удален, но не добавлен.

        Если `force` true - `token` будет только добавлен, но не удален.

        .. code-block:: js

            el.classList.toggle('some-orange-class', theme === 'orange');
            