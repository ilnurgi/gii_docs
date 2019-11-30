.. title:: js boolean

.. meta::
    :description:
        Описание javascript объекта Boolean.
    :keywords:
        js array

Boolean
=======

.. py:class:: Boolean()

    Наследник :py:class:`Object`

    логический тип данных


    .. code-block:: js

        var a = new Boolean();

        1 == 1;
        //true

        'foo' == 'foo';
        //true

        [1,2,3] == [1,2,3];
        //false, потому что разные сущности

        new Array(3) == ",,";
        //true, сравнение со строкой, неявное приведение массива к строке

        new Array(3).toString();
        //",,"

        new Array(3) === ",,";
        //false, сравнение и по типу тоже
