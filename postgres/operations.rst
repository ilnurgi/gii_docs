Операторы
=========

Логические
----------

and
+++

Логическое "И"

Также есть агрегатный вариант оператора :py:func:`bool_and`

.. code-block:: sql

    select
        a and b
    from (
        values
            (false, false),
            (false, true),
            (true, false),
            (true, true),
    ) t(a, b);
    -------
    false
    false
    false
    true

.. code-block:: sql

    select
        a and b
    from (
        values
            (null, false),
            (false, null),
            (null, true),
            (true, null),
            (null, null),
    ) t(a, b);
    -------
    false
    false
    null
    null
    null

not
+++

Логичесое "НЕ"

.. code-block:: sql

    select
        not a
    from (
        values
            (true),
            (false),
            (null)
    ) t(a);
    -------
    false
    true
    null


or
++

Логическое "ИЛИ"

Также есть агрегатный вариант оператора :py:func:`bool_or`

.. code-block:: sql

    select
        a or b
    from (
        values
            (false, false),
            (false, true),
            (true, false),
            (true, true),
    ) t(a, b);
    -------
    false
    true
    true
    true

.. code-block:: sql

    select
        a or b
    from (
        values
            (null, false),
            (false, null),
            (null, true),
            (true, null),
            (null, null),
    ) t(a, b);
    -------
    null
    null
    true
    true
    null


Сравнения
---------

between
+++++++

.. code-block:: sql

    select
        2 between a and b
        , 2 between symmetric a and b
    from (
        values
            (1, 3),
            (3, 1),
    ) t(a, b);
    -------
    true  | true
    false | true


is
++

.. code-block:: sql

    select
        a is null
    from (
        values
            (1),
            (null),
    ) t(a);
    -------
    false
    true

.. code-block:: sql

    select
        a is true is_true
        , a = true eq_true
        , a is not false isnt_false
        , a is false is_false
        , a = false eq_false
        , a is not true isnt_true
    from (
        values
            (true),
            (false),
            (null),
    ) t(a);
    -------
    is_true | eq_true | isnt_false | is_false | eq_false | isnt_true
    false   | false   | false      | true     | true     | true
    true    | true    | true       | false    | false    | false
    false   | null    | true       | false    | null     | true


is distinct from
++++++++++++++++

.. code-block:: sql

    select
        a is distinct from b
    from (
        values
            (1, null),
            (1, 1),
            (null, null),
    ) t(a, b);
    -------
    true
    false
    false
