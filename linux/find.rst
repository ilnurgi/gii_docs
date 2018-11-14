find
====

.. code-block:: sh

	# найти все файлы с расширением mp3
	find . -name "*.mp3"

	# найти все файлы включающих искомую строку, без учета регистра
	find . -iname "ilnurgi"

	# найти все ПАПКИ
	find . -type d -name "ilnurgi"

	# найти все ФАЙЛЫ
	find . -type f -name "ilnurgi"

	# файлы размером
	find . -size 50M
	find . -size +50M -size -100M
