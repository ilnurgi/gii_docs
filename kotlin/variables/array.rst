.. title:: kotlin массивы

.. meta::
    :description lang=ru: описание массивов языка программирования kotlin
    :description lang=en: kotlin arrays description
    :keywords lang=ru: kotlin массивы array
    :keywords lang=en: kotlin array

Массивы
=======

.. code-block:: py

	# массив, в котором может быть null
	val array: Array<Int?> = arrayOf(1,2,3)

	# наловый массив на 10 элементов
	val array: Array<Int?> = arrayOfNulls(10)
	val array = arrayOfNulls<Int?>(10)

	val array = arrayOf(1, 2, 5, 10, 23)
	
	println(array[4])
	# 23

	array[4] = 32
	println(array[4])
	# 32