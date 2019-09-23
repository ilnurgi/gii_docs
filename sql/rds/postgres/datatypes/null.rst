null
====

Функции
-------

coalesce
++++++++

.. code-block:: sql

    select
        coalesce(a, 'no')
    from (
        values
            (null),
            ('yes'),
    ) t(a);
    -------
    no
    yes

nullif
++++++

.. code-block:: sql

    select
        nullif(a, 'no')
    from (
        values
            ('no'),
            ('yes'),
    ) t(a);
    -------
    null
    yes
