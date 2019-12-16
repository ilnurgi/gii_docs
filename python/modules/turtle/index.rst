.. title:: python turtle

.. meta::
    :description:
        Справочная информация по python модулю turtle.
        Модуль для разработки графической части приложения, холст для рисования.
    :keywords:
        python turtle

.. py:module:: turtle

turtle
======

.. toctree::
    :maxdepth: 1

    turtle
    screen

clear()
-------

.. py:function:: clear()


color()
-------

.. py:function:: color(color_name)


hideturtle()
------------

.. py:function:: hideturtle()


penup()
-------

.. py:function:: penup()


register_shape()
----------------

.. py:function:: register_shape(shape_name)

    Регистрирует в системе форму

    .. code-block:: py

        turtle.register_shape('ship.gif')


set_position()
--------------

.. py:function:: set_position(x, y)


write()
-------

.. py:function:: write(text)

    .. code-block:: py

        turtle.write('text', move=False, align='left', font=('Arial', 18, 'normal'))


.. code-block:: py

    import turtle

    # рисуем квадрат
    pen = turtle.Turtle()
    pen.pendown()
    for side in range(3):
        pen.forward(100)
        pen.right(90)
    pen.forward(100)

    player = turtle.Turtle()
    player.penup()

    def moveRight():
        x = player.xcor()
        x += 10
        player.setx(x)

    def moveLeft():
        x = player.xcor()
        x -= 10
        player.setx(x)

    def moveForward():unicorn
        print('something')
        y = player.ycor()
        y += 10
        player.sety(y)

    def moveBackward():
        y = player.ycor()
        y -= 10
        player.sety(y)

    wn = turtle.Screen()
    wn.listen()

    wn.onkey(moveRight, 'd')
    wn.onkey(moveLeft, 'a')
    wn.onkey(moveForward, 'w')
    wn.onkey(moveBackward, 's')

    turtle.done()
    turtle.close()
