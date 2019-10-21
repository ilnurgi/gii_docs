.. title:: python aiohttp

.. meta::
    :description: 
        Справочная информация по python библиотеке aiohttp.
    :keywords: 
        python aiohttp

.. py:module:: aiohttp

aiohttp
=======

ClientSession()
---------------

.. py:class:: ClientSession()

    .. code-block:: py

        async def get(url):
            async with ClientSession() as session:
                async with session.get(url) as response:
                    return response

