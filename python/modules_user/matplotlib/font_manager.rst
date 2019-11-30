.. py:module:: matplotlib.font_manager

.. title:: matplotlib.font_manager

.. meta::
    :description lang=ru: описание модуля matplotlib.font_manager языка программирования python
    :description lang=en: python matplotlib.font_manager module description
    :keywords lang=ru: python matplotlib font_manager
    :keywords lang=en: python matplotlib font_manager

font_manager
============

findfont()
----------

.. py:method:: findfont(font_name)

	Возвращает строку, путь к шрифту

	.. code-block:: py

		font_manager.findfont('Courier New')
		# C:\Windows\Fonts\cour.ttf
		

findSystemFonts()
-----------------

.. py:method:: findSystemFonts()

	Возвращает список строк, пути до системных шрифтов

	.. code-block:: py

		font_manager.findSystemFonts()
		# ['C:\\Windows\\Fonts\\ARIALNB.TTF', 'C:\\Windows\\Fonts\\seguili.ttf', ...]