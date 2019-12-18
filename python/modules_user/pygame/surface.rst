.. title:: python Surface

.. meta::
    :description: python Surface
    :keywords: python Surface

.. py:currentmodule:: pygame

Surface
=======

.. py:class:: Surface((w, h))

    Поверхность

    .. code-block:: py

        surface = Surface((100, 100))


    .. py:method:: blit(surface, rectangle)

    	Нанесение поверхности на поверхность

    	.. code-block:: py

    		window_surface.blit(text_surface, text_rect)
    		

    .. py:method:: fill((r, g, b))

        Заполняет поверхность цветом

        .. code-block:: py

            surface.fill((0, 255, 255))


    .. py:method:: get_rect()

		Возвращает объект :py:class:`pygame.Rect`, размер экрана

		.. code-block:: py

			text_rec = text_surface,get_rect()
