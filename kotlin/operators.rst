.. title:: kotlin.operators

.. meta::
    :description lang=ru: описание операторов языка программирования kotlin
    :description lang=en: kotlin operators description
    :keywords lang=ru: kotlin операторы
    :keywords lang=en: kotlin operators

Операторы
=========

for
---

.. code-block:: py

	val array = arrayOf(1, 2, 3)
	for (i in array){
		println(i)
	}
	for (i in 0 until 100){
		# 100 не включается
		println(i)
	}
	for (i in 100 down to 0){
		# от 100 до 0
		println(i)
	}
	for (i in 100 down to 0 step 2){
		# от 100 до 0 с шагом 2
		println(i)
	}
	for ((index, i) in array.withIndex()){		
		array[index] = 
	}



if
--

.. code-block:: py

	if (a < 40) {
		...
	} else if (a < 60) {
		...
	} else {
		...
	}

.. code-block:: py

	val count: Integer

	count = if (a < 40) {
		40
	} else if (a < 60) {
		50
	} else {
		# обязательный блок
		60
	}

when
----

.. code-block:: py

	val nameOfMonth = "Март"
	val season: String

	when(nameOfMonth) {
		"Декабрь", "Январь", "Февраль" -> {
			season = "Зима"
		}
		else -> {
			season = "Не определен"
		}
	}

	# season = "Не определен""

.. code-block:: py

	val nameOfMonth = "Март"
	val season = when(nameOfMonth) {
		"Декабрь", "Январь", "Февраль" -> {
			"Зима"
		}
		else -> {
			"Не определен"
		}
	}

	# season = "Не определен""

.. code-block:: py

	val nameOfMonth = 4
	val season = when(nameOfMonth) {
		12, 1, 2 -> {
			"Зима"
		}
		in 3..5 -> {
			"Весна"
		}
		else -> {
			"Не определен"
		}
	}

	# season = "Не определен""

.. code-block:: py

	val temp = 80
	val state = when {
		temp < 0 || temp > -10 -> "Твердое"
		temp < 100 -> "Жидкое"
		else -> "Газообразное"
	}

fun
---

.. code-block:: py

	fun max(a: Int, b: Int): Int {
		if (a > b) {
			return a
		} else {
			return b
		}
	}

	fun max(a: Int, b: Int): Int {
		return if (a > b) {
			a
		} else {
			b
		}
	}

	fun max(a: Int, b: Int): Int = if (a > b) a else b

	fun sum(vararg numbers: Int): Int{
		var result = 0
		for (i in numbers){
			result += i
		}
		return result		
	}

	fun modifyString(string: String, modify: (String) -> String): String {
		...
	}

	inline fun modifyString(...){
		...
	}

	# extension func
	fun Int.isAgeValid() = this in 6..100

	fun muWith(list: List<Int>, operation: List<Int>.() -> Unit) {
		list.operation()
	}

	fun muWith(list: Any, operation: Any.() -> Unit) {
		object.operation()
	}

	fun<T> muWith(list: T, operation: T.() -> Unit) {
		object.operation()
	}

	inline fun<T> muWith(list: T, operation: T.() -> Unit) {
		object.operation()
	}

	inline fun<T, R> muWith(list: T, operation: T.() -> R): R {
		return object.operation()
	}


lambda
------

.. code-block:: py

	val sum = {a: Int, b: Int - > a + b}
	val sum: (Int, Int) -> Int = { a, b -> a + b}
	val square: (Int) -> Int = { it + it }
	val square: (Int) -> Unit = { it + it }


let
---

.. code-block:: py

	var name: String? = null

	fun main() {
		name?.let {
			if (it.length > 5) {
				....
			}
		}
	}


with
----

.. code-block:: py

	with(list) {
		add(5)
	}