.. py:module:: matplotlib.markers

.. title:: matplotlib.markers

.. meta::
    :description lang=ru: описание модуля matplotlib.markers языка программирования python
    :description lang=en: python matplotlib.markers module description
    :keywords lang=ru: python matplotlib markers
    :keywords lang=en: python matplotlib markers

markers
=======

MarkerStyle()
-------------

.. py:class:: MarkerStyle(marker=None, fillstyle=None)

	Стиль для маркера, точки

	* marker - строка или список

	* fillstyle - 'full' | 'left' | 'right' | 'bottom' | 'top' | 'none'


	.. py:attribute:: filled_markers

		список известных заполненных маркеров

		.. code-block:: py

			MarkerStyle.filled_markers
			# ('o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X')


	.. py:attribute:: fillstyles

		список известных заполнитилей

		.. code-block:: py

			MarkerStyle.fillstyles
			# ('full', 'left', 'right', 'bottom', 'top', 'none')

	
	.. py:attribute:: markers

		список известных маркеров

		.. code-block:: py

			MarkerStyle.markers
			{
				'.': 'point', 
				',': 'pixel', 
				'o': 'circle', 
				'v': 'triangle_down', 
				'^': 'triangle_up', 
				'<': 'triangle_left', 
				'>': 'triangle_right', 
				'1': 'tri_down', 
				'2': 'tri_up', 
				'3': 'tri_left', 
				'4': 'tri_right', 
				'8': 'octagon', 
				's': 'square', 
				'p': 'pentagon', 
				'*': 'star', 
				'h': 'hexagon1', 
				'H': 'hexagon2', 
				'+': 'plus', 
				'x': 'x', 
				'D': 'diamond', 
				'd': 'thin_diamond', 
				'|': 'vline', 
				'_': 'hline', 
				'P': 'plus_filled', 
				'X': 'x_filled', 
				0: 'tickleft',
				1: 'tickright', 
				2: 'tickup', 
				3: 'tickdown', 
				4: 'caretleft', 
				5: 'caretright',
				6: 'caretup', 
				7: 'caretdown', 
				8: 'caretleftbase', 
				9: 'caretrightbase',
				10: 'caretupbase', 
				11: 'caretdownbase', 
				'None': 'nothing', 
				None: 'nothing', 
				' ': 'nothing', 
				'': 'nothing'
			}


	.. py:method:: get_alt_path()


	.. py:method:: get_alt_transform()


	.. py:method:: get_capstyle()


	.. py:method:: get_fillstyle()


	.. py:method:: get_joinstyle()


	.. py:method:: get_marker()


	.. py:method:: get_path()


	.. py:method:: get_snap_threshold()


	.. py:method:: get_transform()


	.. py:method:: is_filled()


	.. py:method:: set_fillstyle(fillstyle)


	.. py:method:: set_marker(, marker)

