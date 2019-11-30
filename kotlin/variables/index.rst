.. title:: kotlin variables

.. meta::
    :description: kotlin variables
    :keywords: kotlin variables

Переменные и типы данных
========================

* в kotlin нету примитивных типов

.. toctree::
    :maxdepth: 1

    integer
    long    
    string
    boolean
    array
    list
    map


null
----

.. code-block:: text

	# ошибка, нельзя присвоить null переменным
	val name: String = null


.. code-block:: text

	# ошибки не будет, т.к. стоит вопросительный знак
	# говорящий, что тут может быть null
	val name: String? = null

	# будет ошибка в компиляции и программа не скомпилируется
	println(name.length)

	# тут мы скажем компилятору, что мы точно уверены что тут null не будет
	# не рекомендуемый способ, т.к. если будет null будет null pointer exception
	println(name!!.length)

	# рекомендуемый способ, будет просто null
	println(name?.length)


.. code-block:: text

	val name: String? = null

	# length будет иметь нулабельный тип Integer?
	val length = name?.length

	# length будет иметь НЕ нулабельный тип Integer
	val length = name?.length?:0
	println(length)
	# 0


val
---

.. code-block:: text

	val name = "ilnurgi"

	# ошибка
	# для переменных объявленных через val, 
	# нельзя повторно присвоить новые значения
	# это типа константа
	name = "ilnurgi1"


var
---

.. code-block:: text

	var name: String = "ilnurgi"

	# при задании значения, тип можно не указывать
	var name = "ilnurgi"
