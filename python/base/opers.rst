.. title:: python operators

.. meta::
    :description: 
        Справочная информация по операторам языка программирования python.
    :keywords: 
        python operators

Операторы
=========

Условия
-------

.. code-block:: py

    if a == 5:
        pass
    elif a == 6:
        pass
    else:
        pass

Цикл
----

.. code-block:: py
    
    for index in iter:
        if i == 0:
            # прерывание цикла
            break
        elif i == 1:
            # переход на следующую итерацию цикла
            continue
    else:
        # Данный блок выполняется если цикл закончился без break
        pass

.. code-block:: py
    
    while a < 5:
        if a == 1:
            # прерывание цикла
            break
        elif a == 2:
            # переход на следующую итерацию цикла
            continue
    else:
        # Данный блок выполняется если цикл закончился без break
        pass

Перехват ошибок
---------------

.. code-block:: py

    try:
        a = 5/0
    except ValueError:
        pass
    except Exception as err:
        pass
    else:
        # Данный блок выполняется если исключений не возникло
        pass
    finaly:
        # Данный блок выполняется выполняется в любом случае
        pass

Присваивание
------------

.. code-block:: py

    # простое присванивание
    a = 1

    # присваивание внутри сложных операции
    if (n := len(a)) > 10:
        # внутри условия n = len(a)
        pass


Пустышка
--------

.. code-block:: py

    # оператор пустышка, который ничего не делает
    pass


print
-----

.. warning:: с 3 ветки не доступен

.. code-block:: py

    # печатает объект в стандартный поток вывода
    print 1

Другие
------

.. code-block:: py
    
    #!/usr/bin/python
    # установили интерпретатор, который исполнит данный скрипт
    # coding: utf-8
    # установили кодировку файла
