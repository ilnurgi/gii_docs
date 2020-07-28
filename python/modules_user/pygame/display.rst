.. title:: python pygame.display

.. meta::
    :description:
        Справочная информация по python библиотеке pygame, модуль display.
    :keywords:
        python pygame display

.. py:module:: pygame.display

display
=======

.. code-block:: py

    from pygame import display

flip()
------

.. py:function:: flip()

    Отобразить последний отрисованный экран

    .. code-block:::: py

        display.flip()


set_caption()
-------------

.. py:function:: set_caption(caption)

    Устанавливает заголовок окна

    .. code-block:: py

        display.set_caption('Hello PyGame')


set_icon()
----------

.. py:function:: set_icon(surface)

    Устанавливает иконку приложения

    .. code-block:: py

        icon = pygame.image.load('image.png')
        pygame.display.set_icon(img)


set_mode()
----------

.. py:function:: set_mode((higth, width))

    Возвращает экран/поверхность указанных размеров, :py:class:`pygame.Surface`

    .. code-block:: py

        window = display.set_mode((400, 400))
        window = display.set_mode((400, 400), 0, 32)


update()
--------

.. py:function:: update()

    Обновление экрана

    .. code-block:: py

        display.update()
