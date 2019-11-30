.. title:: kotlin списки

.. meta::
    :description lang=ru: описание списков языка программирования kotlin
    :description lang=en: kotlin list description
    :keywords lang=ru: kotlin списки list
    :keywords lang=en: kotlin list

Списки
======

List
----

.. py:class:: List()

	.. code-block:: py

		val listOfNumbers = ArrayList<Int>()
		listOfNumbers.add(10)

		println(listOfNumbers.get(0))
		# 10

		println(listOfNumbers[0])
		# 10

	.. code-block:: py

		val listOfNumbers: mutableList<Int> = ArrayList()
		
		val list = mutableListOf<String>()

		var list = listOf(
			listOf(1, 2, 3, 4),
			listOf(1, 2, 3, 4),
		)

	.. py:method:: average()

		Возвращает среднее значение списка


	.. py:method:: max()

		Возвращает максимальное значение списка


	.. py:method:: min()

		Возвращает минимальное значение списка


MutableList()
-------------

.. py:class:: MutableList()

	.. code-block:: py

		val list = mitableListOf<Int>()

	.. py:method:: add()

		Добавляет значение в список

		.. code-block:: py

			list.add(1)


	.. py:method:: average()

		Возвращает среднее значение


	.. py:method:: first()

		Возвращает первоое значение


	.. py:method:: last()

		Возвращает последнее значение

		
	.. py:method:: max()

		Возвращает максимальное значение


	.. py:method:: min()

		Возвращает минимальное значение