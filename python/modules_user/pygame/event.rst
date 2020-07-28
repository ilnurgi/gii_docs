.. title:: python pygame.event

.. meta::
    :description:
        Справочная информация по python библиотеке pygame, модуль event.
    :keywords:
        python pygame event

.. py:module:: pygame.event

event
=====

.. code-block:: py

    from pygame import event 

get()
-----

.. py:function:: get()

    Возвращает события, :py:class:`Event`

    .. code-block:: py

        events = event.get()


Event()
-------

.. py:class:: Event()

    Событие


    .. py:attribute:: kind

        Тип события

        * :py:attr:`pygame.K_LEFT` - стрелка влево
        * :py:attr:`K_RIGHT` - стрелка вправо
        * :py:attr:`K_SPACE` - пробел
        * :py:attr:`K_q` - q
        * :py:attr:`K_ESCAPE`

        .. code-block:: py

            if event.kind == pygame.K_RIGHT:
                ship.rect.centerx += 1


    .. py:attribute:: type

        Тип события

        * :py:attr:`KEYDOWN` - кнопка нажата
        * :py:attr:`KEYUP` - кнопка отпущена
        * :py:attr:`MOUSEBUTTONDOWN`
        * :py:attr:`QUIT`

        .. code-block:: py

            if event.type == pygame.QUIT:
                sys.exit()
