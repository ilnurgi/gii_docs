Boolean
=======

Логический тип

Имеет 3 состояния:

* true - истина
* false - ложь
* null - неизвестно

Функции
-------

bool_and
++++++++

.. py:function:: bool_and()

    Агрегатный вариант логического оператора "AND"

    .. code-block:: sql

        select bool_and(a) from (values (true), (false)) t(a);
        -------
        false

bool_or
++++++++

.. py:function:: bool_or()

    Агрегатный вариант логического оператора "OR"

    .. code-block:: sql

        select bool_or(a) from (values (true), (false)) t(a);
        -------
        true