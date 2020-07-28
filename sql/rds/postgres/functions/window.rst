.. title:: postgres window functions

.. meta::
    :description: 
        Справочная информация по субд postgres, оконные функции
    :keywords: 
        postgres window functions

Оконные функции
===============

В качестве оконных функции можно использовать и агрегатные функции

.. code-block:: text

    window (
        [partition by ...]
        [order by ...]
        [
            {range | rows}
            {frame_start | between frame_start and frame_end }
        ]
    )
    /*
        frame_start, frame_end
        - unbounded preceding
        - value preceding
        - current row
        - value following
        - unbounded following
    */

.. code-block:: sql

    select
        x
        , sum(x) over()
        , count(x) over()
    from
        generate_series(1, 10) as f(x);

.. code-block:: sql

    select
        x
        , sum(x) over w
        , count(x) over w
    from
        generate_series(1, 10) as f(x)
    window 
        w as ();
    -- по умолчанию
    -- window w as (range between unbounded preceding and current row);

.. code-block:: text

    x  | sum | count
    ---+-----+------
    1  | 55  | 10
    ...
    10 | 55  | 10

.. code-block:: sql

    select
        x
        , sum(x) over w
        , count(x) over w
    from
        generate_series(1, 10) as f(x)
    window 
        w as (rows between unbounded preceding and current row);

.. code-block:: text

    x  | sum | count
    ---+-----+------
    1  | 1   | 1
    2  | 3   | 2
    3  | 6   | 3
    ...
    10 | 55  | 10

.. code-block:: sql

    select
        x
        , sum(x) over w
        , count(x) over w
    from
        generate_series(1, 10) as f(x)
    window 
        w as (rows between current row and unbounded following);

.. code-block:: text

    x  | sum | count
    ---+-----+------
    1  | 55  | 10
    2  | 54  | 9
    3  | 52  | 8
    ...
    10 | 10  | 1

.. code-block:: sql

    select
        x
        , sum(x) over w
        , count(x) over w
    from
        generate_series(1, 10) as f(x)
    window 
        w as (order by x);

.. code-block:: text

    x  | sum | count
    ---+-----+------
    1  | 1   | 1
    2  | 3   | 2
    3  | 6   | 3
    ...
    10 | 55  | 10

cume_dist()
-----------

dense_rank()
------------

first_value()
-------------

Функция возвращает первое значение окна

.. code-block:: sql

    select
        x
        , first_value() over w fv
    from
        generate_series(1, 10) as f(x)
    window
        w as (order by x);

.. code-block:: text

    x  | fv
    ---+---
    1  | 1
    2  | 1
    ...
    10 | 1

lag()
-----

Функция позволяет заглянуть назад

.. code-block:: sql

    select
        x
        -- 1 - на 1 шаг назад
        , lag(x, 1) over w lg1
        -- 2 - на 2 шага назад
        , lag(x, 2) over w lg2
    from
        generate_series(1, 10) as f(x)
    window
        w as (order by x);

.. code-block:: text

    x  | lg1  | lg2
    ---+------+-----
    1  | null | null
    2  | 1    | null
    3  | 2    | 1
    ...
    10 | 9    | 8


last_value()
------------

Функция возвращает последнее значение окна

.. code-block:: sql

    select
        x
        , last_value() over w lv
    from
        generate_series(1, 10) as f(x)
    window
        w as (order by x);

.. code-block:: text

    x  | lv
    ---+---
    1  | 1
    2  | 2
    ...
    10 | 10


lead()
------

Функция позволяет заглянуть вперед

.. code-block:: sql

    select
        x
        -- 1 - на 1 шаг вперед
        , lead(x, 1) over w ld1
        -- 2 - на 2 шага вперед
        , lead(x, 2) over w ld2
    from
        generate_series(1, 10) as f(x)
    window
        w as (order by x);

.. code-block:: text

    x  | ld1  | ld2
    ---+------+-----
    1  | 2    | 3
    2  | 3    | 4
    ...
    8  | 9    | 10
    9  | 10   | null
    10 | null | null


nth_value()
-----------

Возвращает значение по индексу

.. code-block:: sql

    select
        x
        , nth_value(x, 3) over w nv3
        , nth_value(x, 4) over w nv4
    from
        generate_series(1, 10) as f(x)
    window
        w as (order by x);

.. code-block:: text

    x  | nv3  | nv4
    ---+------+-----
    1  | null | null
    2  | null | null
    3  | 3    | null
    4  | 3    | 4
    ...
    10 | 3    | 4

ntile()
-------

percent_rank()
--------------

rank()
------

row_number()
------------

Функция нумерации

.. code-block:: sql

    select
        x
        , row_number() over () rn
    from
        generate_series(1, 10);

.. code-block:: text

    x  | rn
    ---+---
    1  | 1
    ...
    10 | 10

