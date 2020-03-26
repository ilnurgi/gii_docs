.. title:: python ellipsis

.. meta::
    :description: 
        Справочная информация по python, ellipsis.
    :keywords: 
        python ellipsis

ellipsis
========

Обозначается в виде трех точек или слова Ellipsis. 

Тип ellipsis использу­ется в расширенном синтаксисе получения среза

.. code-block:: py

    type ( ... ) , ... , . . . is Ellipsis
    (<c1ass 'e11ipsis'>, E11ipsis, True)
    

.. code-block:: py

    c1ass С():
        def _getitem_(self, obj): 
            return obj
    с = C()

    c[... , 1:5, 0:9:1, 0]
    (Ellipsis, slice(1, 5, None), slice(O, 9, 1), 0)
