ndarray
=======

.. py:class:: ndarray

    Экземпляры данного класса возвращают методы модуля

    .. code-block:: py

        a = array([10])


    .. py:attribute:: dtype

        Тип значений массива

        .. code-block:: py

            array([10]).dtype
            # int64


    .. py:attribute:: itemsize

        Возвращает число, размер одного элемента массива

        .. code-block:: py

            numpy.random.randint(10, size=(3, 4, 5)).itemsize
            # 8


    .. py:attribute:: nbytes

        Возвращает число, размер всех значений массива

        .. code-block:: py

            numpy.random.randint(10, size=(3, 4, 5)).nbytes
            # 480


    .. py:attribute:: ndim

        .. code-block:: py

            array([
                [4, 8], 
                [10, 20]
            ]).ndim
            # 2


    .. py:attribute:: shape

        Размерность массива

        .. code-block:: py

            array(
                [
                    [2, 4, 6, 8],
                    [3, 3, 2, 1],
                    [2, 6, 3, 4],
                    [5, 2, 3, 5]
                ]
            ).shape
            # (4, 4)


    .. py:attribute:: size

        Количесвто элементов в массиве

        .. code-block:: py

            numpy.random.randint(10, size=(3, 4, 5)).size
            # 60


    .. py:method:: argmax([axis])

        Индекс максимального элемента

        .. code-block:: py

            array([2, 1, 9]).argmax()
            # 2


    .. py:method:: argmin([axis])

        Индекс минимального элемента

        .. code-block:: py

            array([2, 1, 9]).argmin()
            # 1


    .. py:method:: clip(min, max)

        Сокращение

        .. code-block:: py

            array([6, 2, 5, -1, 0]).clip(0, 5)
            # array([5, 2, 5, 0, 0])


    .. py:method:: diagonal()

        Получить диагональ

        .. code-block:: py

            array([[1, 2], [3, 4]]).diagonal()
            # array([ 1, 4])


    .. py:method:: dot(array)

        .. code-block:: py

            array([2, 4]).dot(array([2, 4]))
            # 20


    .. py:method:: mean()

        Возвращает новый массив средних значений

        .. code-block:: py

            sample = normal(loc=[2., 20.], scale=[1., 3.5], size=(3, 2))
            """
            array(
                [
                    [ 1.816 , 23.703 ],
                    [ 2.8395, 12.2607],
                    [ 3.5901, 24.2115]
                ]
            )
            """

            sample.mean(axis=0)
            # array([2.7486, 20.0584])

            array([2, 1, 9]).mean()
            # 4


    .. py:method:: prod()

        Умножение элементов матриц

        .. code-block:: py

            array([2, 3, 4]).prod()
            # 24


    .. py:method:: reshape(size: tuple)

        Изменяет размерность массива

        .. code-block:: py

            arange(1, 10).reshape((3, 3))
            """
            array([
                [1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]
            ])
            """

            array([1, 2, 3]).reshape((1, 3))
            # array([[1, 2, 3]])


    .. py:method:: sort()

    .. py:method:: std()

        Девиация

        .. code-block:: py

            array([2, 1, 9]).std()
            # 3.559


    .. py:method:: sum()

        Возвращает новый сложенный массив

        .. code-block:: py

            arr = array(
                [
                    [1, 2, 3],
                    [10, 20, 30]
                ]
            )
            
            arr.sum(axis=0)
            // array([11, 22, 33])

            arr.sum(axis=1)
            // array([6, 60])

            array([2, 4, 3]).sum()
            # 9


    .. py:method:: to_list()

        Возвращает содержимое в виде объекта :py:class:`list`

        .. code-block:: py

            a.to_list()
            # [10]


    .. py:method:: var()

        Вариация

        .. code-block:: py

            array([2, 1, 9]).var()
            # 12.666