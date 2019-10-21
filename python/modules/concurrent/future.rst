.. title:: python concurrent futures

.. meta::
    :description: 
        Справочная информация по python библиотеке concurrent.futures.
    :keywords: 
        python concurrent futures

.. py:module:: concurrent.futures

futures
=======

ThreadPoolExecutor()

.. py:class:: ThreadPoolExecutor()

    .. code-block:: py

        with ThreadPoolExecutor(max_workers=4) as executor:

            futures = [
                executor.submit(
                    lambda: requests.get('http://ilnurgi.ru')

                ) for _ in range(8)
            ]

        results = [
            f.result().status_code
            for f in futures
        ]