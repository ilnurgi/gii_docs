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


set_mode()
----------

.. py:function:: set_mode((higth, width))

    Возвращает экран/поверхность указанных размеров, :py:class:`pygame.Surface`

    .. code-block:: py

        window = display.set_mode((400, 400))
        window = display.set_mode((400, 400), 0, 32)


set_caption()
-------------

.. py:function:: set_caption(caption)

    Устанавливает заголовок окна

    .. code-block:: py

        display.set_caption('Hello PyGame')

update()
--------

.. py:function:: update()

	Обновление экрана

	.. code-block:: py

		display.update()
		