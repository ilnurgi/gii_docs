.. py:module:: pygame.event

event
=====

.. code-block:: py

    from pygame import event 

get
---

.. py:function:: get()

    Возвращает события, :py:class:`Event`

    .. code-block:: py

        events = event.get()


Event
-----

.. py:class:: Event()

    Событие


    .. py:attribute:: kind

        Тип события

        * K_LEFT - стрелка влево
        * K_RIGHT - стрелка вправо
        * K_SPACE - пробел
        * K_q - q
        * K_ESCAPE

        .. code-block:: py

            if event.kind == pygame.K_RIGHT:
                ship.rect.centerx += 1


    .. py:attribute:: type

        Тип события

        * KEYDOWN - кнопка нажата
        * KEYUP - кнопка отпущена
        * MOUSEBUTTONDOWN
        * QUIT

        .. code-block:: py

            if event.type == pygame.QUIT:
                sys.exit()