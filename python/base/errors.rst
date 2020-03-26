.. title:: python exceptions

.. meta::
    :description: 
        Справочная информация по python, exceptions.
    :keywords: 
        python exceptions

exceptions
==========

.. code-block:: py
    try:
        5/0
    except ZeroDivisionError as err:
        print err

.. code-block:: py

    raise RuntimeError(u'Ошибка какая то')

.. code-block:: py

    class MyException(Exception): pass

.. code-block:: py

    assert False, u'Данная строка возбудит исключение AssertionError'


AttributeError()
----------------

.. py:class:: AttributeError

    Возбуждается при обращении к несуществующему атрибуту

    Наследник :py:class:`StandardError`


ArithmeticError()
-----------------

.. py:class:: ArithmeticError

    Базовый класс исключений, возбуждаемых арифметическими операциями

    Наследник :py:class:`StandardError`


AssertionError()
----------------

.. py:class:: AssertionError

    Возбуждается инструкциями assert

    Наследник :py:class:`StandardError`


BaseException()
---------------

.. py:class:: BaseException

    Базовый класс всех исключений


EnvironmentError()
------------------

.. py:class:: EnvironmentError

    Ошибка, обусловленная внешними причинами

    Наследник :py:class:`StandardError`


EOFError()
----------

.. py:class:: EOFError

    Возбуждается по достижении конца файла

    Наследник :py:class:`StandardError`


Exception()
-----------

.. py:class:: Exception

    Базовый класс для всех исключений, не связанных с завершением программы

    Наследник :py:class:`BaseException`


FloatingPointError()
--------------------

.. py:class:: FloatingPointError

    Ошибка в инструкции import

    Наследник :py:class:`ArithmeticError`


GeneratorExit()
---------------

.. py:class:: GeneratorExit

    Возбуждается методом .close() генераторов

    Наследник :py:class:`BaseException`


ImportError()
-------------

.. py:class:: ImportError

    Ошибка в инструкции import

    Наследник :py:class:`SyntaxError`


IndentationError()
------------------

.. py:class:: IndentationError

    Ошибка оформления отступов

    Наследник :py:class:`SyntaxError`


IndexError()
------------

.. py:class:: IndexError

    Ошибка обращения по индексу за пределами последовательности.

    Наследник :py:class:`LookupError`


IOError()
---------

.. py:class:: IOError

    Ошибка ввода-вывода при работе с файлами

    Наследник :py:class:`EnvironmentError`


KeyError()
----------

.. py:class:: KeyError

    Ошибка обращения к несуществующему ключу словаря

    Наследник :py:class:`LookupError`


KeyboardInterrupt()
-------------------

.. py:class:: KeyboardInterrupt

    Возбуждается нажатием клавишей прерывания (обычно Ctrl-C)

    Наследник :py:class:`BaseException`


LookupError()
-------------

.. py:class:: LookupError

    Ошибка обращения по индексу или ключу

    Наследник :py:class:`Exception`


MemoryError()
-------------

.. py:class:: MemoryError

    Нехватка памяти

    Наследник :py:class:`Exception`


NameError()
-----------

.. py:class:: NameError

    Не удалось отыскать локальное или глобальное имя

    Наследник :py:class:`Exception`


NotImplementedError()
---------------------

.. py:class:: NotImplementedError

    Обращение к нереализованному методу или функции

    Наследник :py:class:`Exception`


OSError()
---------

.. py:class:: OSError

    Ошибка операционной системы

    Наследник :py:class:`EnvironmentError`


ReferenceError()
----------------

.. py:class:: ReferenceError

    Ошибка обращения к объекту, который уже был уничтожен

    Наследник :py:class:`Exception`


RuntimeError()
--------------

.. py:class:: RuntimeError

    Универсальное исключение

    Наследник :py:class:`Exception`


StandardError()
---------------

.. py:class:: StandardError

    Базовый класс для всех встроенных исключений (только в Python 2).

    В Python 3 – базовый класс всех исключений, наследующих класс Exception

    Наследник :py:class:`Exception`


StopIteration()
---------------

.. py:class:: StopIteration

    Возбуждается для прекращения итераций

    Наследник :py:class:`Exception`


SyntaxError()
-------------

.. py:class:: SyntaxError

    Синтаксическая ошибка

    Наследник :py:class:`Exception`


SystemError()
-------------

.. py:class:: SystemError

    Нефатальная системная ошибка в интерпретаторе

    Наследник :py:class:`Exception`


SystemExit()
------------

.. py:class:: SystemExit

    Завершение программы

    Наследник :py:class:`BaseException`


TabError()
----------

.. py:class:: TabError

    Непоследовательное использование символа табуляции (генерируется при запуске интерпретатора с ключом –tt)

    Наследник :py:class:`IndentationError`


TypeError()
-----------

.. py:class:: TypeError

    Попытка выполнить операцию над аргументом недопустимого типа

    Наследник :py:class:`Exception`


UnboundLocalError()
-------------------

.. py:class:: UnboundLocalError

    Ошибка обращения к локальной переменной, которой еще не было присвоено значение

    Наследник :py:class:`Exception`


UnicodeError()
--------------

.. py:class:: UnicodeError

    Ошибка при работе с символами Юникода

    Наследник :py:class:`ValueError`


UnicodeDecodeError()
--------------------

.. py:class:: UnicodeDecodeError

    Ошибка декодирования символов Юникода

    Наследник :py:class:`ValueError`


UnicodeEncodeError()
--------------------

.. py:class:: UnicodeEncodeError

    Ошибка кодирования символов Юникода

    Наследник :py:class:`ValueError`


UnicodeTranslateError()
-----------------------

.. py:class:: UnicodeTranslateError

    Ошибка трансляции символов Юникода

    Наследник :py:class:`ValueError`


ValueError()
------------

.. py:class:: ValueError

    Недопустимый тип

    Наследник :py:class:`Exception`


ZeroDivisionError()
-------------------

.. py:class:: ZeroDivisionError

    Деление или деления по модулю на ноль

    Наследник :py:class:`ArithmeticError`
