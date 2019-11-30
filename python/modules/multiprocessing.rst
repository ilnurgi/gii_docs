.. py:module:: multiprocessing

multiprocessing
===============


Pool
----

.. py:class:: Pool(processes=cpu_count())

    .. code-block:: py

        pool = Pool(2)

        with Pool() as pool:

            pool.map(func, args)


    .. py:class:: ApplyResult()

        .. py:method:: get()

            возвращает значение результата


    .. py:method:: apply(func, args)

        .. code-block:: py

            result = [pool.apply(some_func, args=(num, )) for num in [1, 2, 3]]


    .. py:method:: apply_async(func, args)

        Возвращает :py:class:`ApplyResult`

        .. code-block:: py

            result = [pool.apply_async(some_func, args=(num, )) for num in [1, 2, 3]]


    .. py:method:: close()

        .. code-block:: py

            pool.close()


    .. py:method:: join()

        .. code-block:: py

            pool.join()


    .. py:method:: map(func, iterable)

        .. code-block:: py

            pool.map(some_func, [1,2,3])


    .. py:method:: starmap()

        .. code-block:: py

            pool.starmap(sum, [(1, 6), (2, 7)])


    .. py:method:: starmap_async()



cpu_count()
-----------

.. py:method:: cpu_count()

    Возвращает количество ядер процессора

    .. code-block:: py

        cpu_count()
        # 4


current_process
---------------

.. py:method:: current_process()

    Возвращает текущий процесс


