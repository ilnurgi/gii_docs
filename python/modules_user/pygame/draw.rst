.. py:module:: pygame.draw

draw
====

.. code-block:: py

	from pygame import draw


circle
------

.. py:method:: circle(surface, color, center, radius, ?)

	Рисует окружность

	.. py:method:: py

		draw.circle(window_surface, (0, 0, 0), (300, 50), 20, 0)


ellipse
-------

.. py:method:: ellipse(surface, color, points, ?)

	Рисует эллипс

	.. code-block:: py

		draw.ellipse(window_surface, (0, 0, 0), (300, 350, 560, 100), 2)


line
----

.. py:method:: line(surface, color, point1, point2, ?)

	Рисует линию

	.. code-block:: py

		draw.line(window_surface, (0, 0, 0), (60, 50), (120, 70), 5)


polygon
-------

.. py:method:: polygon(surface, color, rect)

	Рисут многоугольник

	.. code-block:: py

		draw.polygon(window_surface, (0, 0, 0), ((146, 0), (236, 277)))


rect
----

.. py:method:: rect(surface, color, rect)

	Рисует прямоугольную область

	.. code-block:: py

		draw.rect(window_surface, (0, 0, 0), (0, 10, 10, 0))
