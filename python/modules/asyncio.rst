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

    .. code-block:: py

        loop = get_event_loop()

        coroutines = [async_get(url) for _ in range(8)]

        results = loop.run_until_complete(asyncio.gather(*coroutines))