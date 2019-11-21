.. title:: python asyncio

.. meta::
    :description: 
        Справочная информация по python библиотеке asyncio.
    :keywords: 
        python asyncio

.. py:module:: asyncio

asyncio
=======

get_event_loop()
----------------

.. py:function:: get_event_loop()

    Возвращает цикл обработчика событий

    .. code-block:: py

        loop = get_event_loop()

        coroutines = [async_get(url) for _ in range(8)]

        results = loop.run_until_complete(asyncio.gather(*coroutines))


loop()
------

.. py:class:: loop()

    Объект цикла, возвращаемого :py:meth:`get_event_loop()`

    .. py:method:: run_until_complete()

        .. code-block:: py

            async def task():
                print('hello world')
            
            async def task2():
                print('hello world')

            loop.run_until_complete(task())
            
            loop.run_until_complete(asyncio.gather(task(), task2()))

sleep()
-------

.. py:method:: sleep()

    Асинхронный метод ожидания

    .. code-block:: py

        async def runner():

            while True:
                before()
                asyncio.sleep(1)
                after()

                