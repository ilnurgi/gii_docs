Арифметические операции
=======================

.. code-block:: py

    array([1, 2, 3]) + array([4, 5, 6])
    # array([5, 7, 9])

    array([1, 2, 3]) * 1.5
    # array([1.5,  3.,  4.5])

    array([2]) * array([[1, 2], [3, 4]])
    # array([[2, 4], [6, 8]])

    array([1.5, 2.5, 3.5]) / array([10., 5., 1.])
    # array([0.15, 0.5 , 3.5 ])


e
-

pi
--

abs()
-----

add()
-----

.. py:function:: add() 

    Сложение, 1 + 1

    .. code-block:: py

        arange(4) + 5
        # array([5, 6, 7, 8])


arccos()
--------

arccosh()
---------

arcsin()
--------

arcsinh()
---------

arctan()
--------

arctanh()
---------

cos()
-----

cosh()
------

divide()
--------

.. py:function:: divide() 

    Деление, 1 / 1


exp()
-----

floor_divide()
--------------

.. py:function:: floor_divide() 

    Целочисленное от деления, 1 // 1


log()
-----

log10()
-------

max()
-----

min()
-----

mod()
-----

.. py:function:: mod() 

    Остаток от деления, 1 % 1


multiply()
----------

.. py:function:: multiply() 

    Умножение, 1 * 1


negative(
----------

.. py:function:: negative() 

    Отрицательное значение, -1


power()
-------

.. py:function:: power() 

    Возведенеи в степень, 1 ** 1


prod()
------

sign()
------

sin()
-----

sinh()
------

sqrt()
------

subtract()
----------

.. py:function:: subtract() 

    Вычитание, 1 - 1

    .. code-block:: py

        arange(4) - 5
        # array([-5, -4, -3, -2])

sum()
-----

tan()
-----

tanh()
------