.. title:: python set

.. meta::
    :description: 
        Справочная информация по python, set.
    :keywords: 
        python set

set
===

.. py:class:: set()

    Множества используются для хранения неупорядоченных коллекций уникальных объектов.

    Множество может содержать только элементы неизменяемых типов,
    например числа, строки, кортежи.

    .. code-block:: py

        set([1,1,1,1,2])
        # {1, 2}

        set('abc')
        # {'a', 'b', 'c'}

        {'abc'}
        # {'abc'}

        {1, 2, 3}
        # {1, 2, 3}

        {(1, 1), (1, 1), (1, 2)}
        # {(1, 1), (1, 2)}

        len({1, 1, 2})
        # 2

        1 in {1, 1, 2}
        # True

        3 in {1, 1, 2}
        # False

    .. py:method:: add(obj)

        Добавляет новый объект в множество

        .. code-block:: py

            {1, 2}.add(3)
            # {1, 2, 3}


    .. py:method:: clear()

        Очищает множество

        .. code-block:: py

            {1, 2}.clear()
            # {}


    .. py:method:: copy()

        Возвращает копию объекта

        .. code-block:: py

            {1, 2}
            # {1, 2}


    .. py:method:: difference(iterable1, iterable2, ...)

        Возвращает :py:class:`set`, разницу между множеством и итерируемым объектом

        .. code-block:: py

            {1, 2, 3}.difference([1, 2, 4])
            # {3}

            {1, 2, 3} - {1, 2, 4}
            # {3}


    .. py:method:: difference_update(iterable1, iterable2, ...)

        Удаляет элементы множества, которые присутствуют в обоих множествах

        .. code-block:: py

            {1,2,3}.difference_update(set([1,2,4]))
            # s = {3}

            s -= set([3,4,5])
            # s = {}


    .. py:method:: discard(obj)

        Удаляет объект из множества, если объекта в множестве нет, исключения не будет, как при remove

        .. code-block:: py

            {1, 2}.discard(3)
            # {1, 2}            


    .. py:method:: intersection(iterable1, iterable2, ...)

        Возвращает множество :py:class:`set`, элементы которого существуют в указанных объектах

        .. code-block:: py

            {1, 2, 3}.intersection([1,2,4])
            # {1, 2 }

            {1, 2, 3} & set([1,2,4])
            # {1, 2}


    .. py:method:: intersection_update(iterable1, iterable2, ...)

        В исходном множестве останутся только которые, которые есть в обоих множествах

        .. code-block:: py

            {1, 2, 3}.intersection_update([1, 2, 4])
            # {1, 2}

            s &= {1, 6, 7}
            # {1}


    .. py:method:: isdisjoint(iterable)

        Возвращает :py:class:`bool`, множества не имеют одинаковых элементов

        .. code-block:: py

            {1, 2, 3}.isdisjoint([4, 5, 6])
            # True

            {1, 2, 3}.isdisjoint([4, 5, 1])
            # False

            bool({1, 2, 3} & {4, 5, 6})


    .. py:method:: issubset(iterable)

        Возвращает :py:class:`bool`, входит ли исходное множество в указанное

        .. code-block:: py

            {1, 2, 3}.issubset([1,2,3,4])
            # True

            {1, 2, 3} <= {1, 2, 3}
            # True

            {1, 2, 3} <= {1, 2, 3, 4}
            # True

            {1, 2, 3} < {1, 2, 3}
            # False

            {1, 2, 3} < {1, 2, 3, 4}
            # True


    .. py:method:: issuperset(iterable)

        Возвращает :py:class:`bool`, входит ли указанное множество в исходное множество

        .. code-block:: py

            {1, 2, 3}.issuperset([1,2])
            # True

            {1, 2, 3} >= {1, 2}
            # True

            {1, 2, 3} >= {1, 2, 3}
            # True

            {1, 2, 3} > {1, 2}
            # True

            {1, 2, 3} > {1, 2, 3}
            # False


    .. py:method:: pop()

        Возвращает произвольный объект множества, удалив его из множества

        .. code-block:: py

            {1, 2, 3}.pop()
            # 2

            set().pop()
            # KeyError


    .. py:method:: remove(obj)

        Удаляет объект из множества

        .. code-block:: py

            {1, 2}.remove(1)
            # {2}

            {1, 2}.remove(3)
            # KeyError


    .. py:method:: symmetric_difference(iterable)

        Возвращает множество :py:class:`set`, которое не содержит одинаковых элементов в обоих объектах

        .. code-block:: py

            {1, 2, 3}.symmetric_difference([1, 2, 4])
            # {3, 4}

            {1, 2, 3} ^ {1, 2, 4} ^ {1, 2, 5}
            # {3, 4, 5}


    .. py:method:: symmetric_difference_update(iterable)

        Оставляет в исходном множестве все элементы, кроме одинаковых

        .. code-block:: py

            {1,2,3}.symmetric_difference_update([1,2,4])
            # {3, 4}

            {1, 2, 3} ^= {1, 2, 4}
            # {3, 4}


    .. py:method:: union(iterable1, iterable2, ...)

        Возвращает новое множество :py:class:`set`, объединенное c переданным итерируемым объектом

        .. code-block:: py

            {1, 2, 3}.union([4, 5, 6])
            # {1, 2, 3, 4, 5, 6}

            {1, 2, 3}.union([4, 5, 6], (6, 5, 4))
            # {1, 2, 3, 4, 5, 6}

            {1, 2, 3} | set([4, 5, 6])
            # {1, 2, 3, 4, 5, 6}


    .. py:method:: update(iterable1, iterable2, ...)

        Добавляет в множество новые элементы

        .. code-block:: py

            {1, 2, 3}.update([4,5,6], (7, 8))
            # {1, 2, 3, 4, 5, 6, 7, 8}

            s |= {9}
            # {1, 2, 3, 4, 5, 6, 7, 8, 9}

    .. py:method:: remove(obj)



Генератор множеств
------------------

.. versionadded:: 3.x

.. code-block:: py

    { i for i in [1,2,3,1]}
    # {1,2,3}