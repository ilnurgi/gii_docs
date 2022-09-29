.. py:module:: kivy.utils

utils
=====

platform
--------

.. py:attribute:: platform

	.. code-block:: py

		platform
		# linux


boundary()
----------


.. py:function:: boundary(value, minvalue, maxvalue)



deprecated()
------------

.. py:function:: deprecated(func=None, msg='')



difference()
------------

.. py:function:: difference(set1, set2)



escape_markup()
---------------

.. py:function:: escape_markup(text)



get_color_from_hex()
--------------------

.. py:function:: get_color_from_hex(s)



get_hex_from_color()
--------------------

.. py:function:: get_hex_from_color(color)

	.. code-block:: py

		get_hex_from_color((0, 1, 0))
		# '#00ff00'
		get_hex_from_color((.25, .77, .90, .5))
		# '#3fc4e57f'


get_random_color()
------------------

.. py:function:: get_random_color(alpha=1.0)


	.. code-block:: py

		get_random_color(alpha=1.0)
		get_random_color(alpha='random')


interpolate()
-------------

.. py:function:: interpolate(value_from, value_to, step=10)


intersection()
--------------

.. py:function:: intersection(set1, set2)



is_color_transparent()
----------------------

.. py:function:: is_color_transparent(c)



relify()
--------

.. py:function:: relify(func)



rgba()
------

.. py:function:: rgba(s, *args)



strtotuple()
------------

.. py:function:: strtotuple(s)


	.. code-block:: py

		strtotuple(str((12, 45, 56)))
		# (12, 45, 56)

		
SafeList()
----------

.. py:class:: SafeList(iterable=())


QueryDict()
-----------

.. py:class:: QueryDict()

	Обычный словарь, обращение к ключам возможно через точку

	.. py:code:: py

		d = QueryDict()
		d.a = 1
		d['a']
		# 1
