.. title:: python turtle Turtle

.. meta::
    :description:
        Справочная информация по python модулю turtle.
        Модуль для разработки графической части приложения, холст для рисования.
        Turtle - кисть для рисования.
    :keywords:
        python turtle Turtle

.. py:currentmodule:: turtle


Turtle()
========

.. py:class:: Turtle()

    .. code-block:: py

        # "кисточка" для рисования
        pen = Turtle()


    .. py:method:: backward()
    .. py:method:: color(color)

        Устанавливает цвет кисти

        .. code-block:: py

            pen.color('red')


    .. py:method:: forward(steps)

        Перемещаем кисточку на указанное количество шагов.

        .. code-block:: py

            pen.forward(100)


    .. py:method:: hideturtle()

        Скрывает указатель

        .. code-block:: py

            pen.hideturtle()


    .. py:method:: left()
    .. py:method:: pendown()

        Опускам "кисточку" на холст

        .. code-block:: py

            pen.pendown()


    .. py:method:: penup()
    .. py:method:: right(deg)

        Поворачивает кисть вправо на указанное количество градусов.

        .. code-block:: py

            pen.right(90)


    .. py:method:: setheading()

        .. code-block:: py

            pen.setheading(90)


    .. py:method:: setposition(x, y)

        Устаналивает позицию кисти

        .. code-block:: py

            pen.setposition(-300, 300)


    .. py:method:: setx(x)

        Устанавливает новую координату х для кисти

        .. code-block:: py

            pen.setx(100)

            
    .. py:method:: sety(y)


    .. py:method:: shape(shape_name)

        Задаем указателю новую зарегистрированную форму

        .. code-block:: py

            turtle.register_shape('ship.gif')


    .. py:method:: shapesize()

        .. code-block:: py

            pen.shapesize(2, 2)


    .. py:method:: speed()

        .. code-block:: py

            pen.speed(0)


    .. py:method:: xcor()

        Возвращает координату х объекта

        .. code-block:: py

            x = pen.xcor()
            pen.setx(x+10)


    .. py:method:: ycor()
