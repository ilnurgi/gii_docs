.. title:: kotlin мапы

.. meta::
    :description lang=ru: описание мапов языка программирования kotlin
    :description lang=en: kotlin map description
    :keywords lang=ru: kotlin мапы map
    :keywords lang=en: kotlin map

Мапы
====

Map()
-----

.. py:class:: Map()

	.. code-block:: py

		val data = mutableMapOf<String, List<Int>>()
		data["key"] = listOf(1, 2, 4)

		val data = mapOf (
			"key" listOf(1, 2, 3)
		)

		val data = mapOf (
			Pair("key", listOf(1, 2, 3))
		)

	.. py:attribute:: keys

		Возвращает ключи :py:class:`Set`


	.. py:method:: filter(predicat)

		Возвращает новый объект :py:class:`Map` отфильтровый по условию

		.. code-block:: py

			data.filter { it.value.any { it < 0} }
			

	.. py:method:: filterNot(predicat)

		Возвращает новый объект :py:class:`Map` отфильтровый по условию

		.. code-block:: py

			data.filterNot { it.value.any { it < 0} }


	.. py:method:: flatMap()

		Возвращает новый развернутый объект :py:class:`Map`

		.. code-block:: py

			data.flatMap { it.value }


	.. py:method:: map()

		Возвращает новую мапу :py:class:`Map` с преобразованными данными

		.. code-block:: py

			data.map { it.value.sum() }
