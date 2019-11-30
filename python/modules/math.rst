.. title:: python math

.. meta::
    :description: 
        Справочная информация по python модулю math.
    :keywords: 
        python math

.. py:module:: math

math
====

Модуль для работы с арифметическими функциями 

pi
--

.. py:attribute:: pi
    
    Возвращает значение  `pi`
  
    .. code-block:: py  
    
        math.pi
        # 3.141592653589793

e
-

.. py:attribute:: e

    Возвращает число `e`

    .. code-block:: py
    
        math.e
        # 2.718281828459045

acos()
------

.. py:function:: acos(x) 
    
    Возвращает арккосинус угла в радианах, заданного градуса


acosh()
-------

.. py:function:: acosh(x) 
    
    Возвращает гиперболический арккосинус числа Х 


asin()
------

.. py:function:: asin(x) 

    Возвращает арксинус угла в радианах, заданного градуса


asinh()
-------

.. py:function:: asinh(x) 

    Возвращает гиперболический арксинус числа Х 


atan()
------

.. py:function:: atan(x) 
    
    Возвращает арктангенс угла в радианах, заданного градуса


atan2()
-------

.. py:function:: atan2(x, y) 
    
    Возвращает арктангенс выражения (x/y). Эквивалентно atan(x/y). Аргумент y может быть равен нулю - в этом случае возвращается pi/2. 

atanh()
-------

.. py:function:: atanh(x) 
    
    Возвращает гиперболический арктангенс числа Х 

ceil()
------

.. py:function:: ceil() 

    Возвращает округленно до наибольшего целого значения числа.
    
    .. code-block:: py
        
        math.ceil(3.14)
        # 4

copysign()
----------

.. py:function:: copysign(x, y) 

    Возвращает х с тем же знаком что и у.

cos()
-------

.. py:function:: cos(x) 

    Возвращает косинус числа, заданного в радианах

cosh()
------

.. py:function:: cosh(x) 

    Возвращает гиперболический косинус числа

degrees()
---------

.. py:function:: degrees(x) 

    Преобразует радианы в значение угла


dist()
------

.. py:function:: dist()

    .. versionadded:: 3.8

    Возвращает расстояние между точками

    .. code-block:: py

        math.dist((16, 25, 20), (8, 15, 14))
        # 14.142


exp()
-----

.. py:function:: exp(x) 

    Возвращает e ** x


fabs()
------

.. py:function:: fabs(x) 
    
    Возвращает абсолютное значение числа x 


factorial()
-----------

.. py:function:: factorial(x) 
    
    Возвращает факториал числа x 


floor()
-------

.. py:function:: floor() 
    
    Возвращает округленное до наименьшего целого значение числа
    
    .. code-block:: py

        math.floor(3.14)
        # 3


fmod()
------

.. py:function:: fmod(x, y) 
    
    Возвращает остаток от деления x на y и эквивалентно x%y 


frexp()
-------

.. py:function:: frexp(x) 
    
    Возвращает пару чисел в виде кортежа (m, e), где m - мантисса (вещественное число), а e - экспоненциальная часть (целое число). Для чисел m и e всегда выполняется условие x=m*2**e. Если аргумент x равен нулю, возвращает (0.0, 0). В противном случае всегда выполняется 0.5<=abs<1 


fsum()
------

.. py:function:: fsum(iter) 
    
    Возвращает сумму значений с плавающей точкой в итерируемой последовательности.


hypot()
-------

.. py:function:: hypot(x, y) 

    Возвращает длину гипотенузы прямоугольника со сторонами длиной x и y и эквивалентно sqrt(x*x+y*y) 

    .. code-block:: py

        math.hypot(16, 25, 20)
        # длина вектора
        # 35.791

        math.hypot(8, 15, 14)
        # длина вектора
        # 22.028


isin()
------

.. py:function:: isin(x) 

    Возвращает True, если значение бесконечность


isnan()
-------

.. py:function:: isnan(x) 

    Возвращает True, если значение NaN


isqrt()
-------

.. py:function:: isqrt()

    .. versionadded:: 3.8

    Возвращает целую часть корня

    .. code-block:: py

        math.sqrt(15)
        # 3.872

        math.isqrt(15)
        # 3


ldexp()
-------

.. py:function:: ldexp(m, e) 
    
    Функция обратная .. py:function:: 'frexp' и возвращает m*(2**e) 


log()
-----

.. py:function:: log(x [, base]) 
    
    Возвращает натуральный логарифм числа x


log10()
-------

.. py:function:: log10(x) 
    
    Возвращает десятичный логарифм числа x 


log1p()
-------

.. py:function:: log1p(x) 
    
    Возвращает натуральный логарифм выражения x + 1


modf()
------

.. py:function:: modf(x) 
    
    Возвращает дробную и целую части числа x в виде кортежа. Оба значения имеют тот же знак, что и число x.


pow()
-----

.. py:function:: pow(x, y) 
    
   Возвращает x ** y


prod()
------

.. py:function::  prod(iterable)

    .. versionadded:: 3.8

    Возвращаем перемноженное значение

    .. code-block:: py

        2 * 8 * 7 * 7 == math.prod((2, 8, 7, 7))
        # True

radians()
---------

.. py:function:: radians(x) 

    Преобразует значение в радианы


sin()
-----

.. py:function:: sin(x) 

    Возвращает синус угла, заданного в радианах


sinh()
------

.. py:function:: sinh(x) 

    Возвращает гиперболический синус числа x 


sqrt()
------

.. py:function:: sqrt() 
    
    Возвращает корень из числа.

    :py:func:`math.isqrt` 

    .. code-block:: py
        
        math.sqrt(9)
        # 3.0

        math.sqrt(15)
        # 3.873


tan()
-----

.. py:function:: tan(x) 
    
    Возвращает тангенс угла, заданного в радианах


tanh()
------

.. py:function:: tanh(x) 
    
    Возвращает гиперболический тангенс числа x.


trunc()
-------

.. py:function:: trunc(x)

    Усекает дробную часть числа.