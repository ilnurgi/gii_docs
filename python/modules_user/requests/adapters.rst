.. title:: python requests adapters

.. meta::
    :description: 
        Справочная информация по python библиотеке requests.adapters.
    :keywords: 
        python requests,
        python requests adapters

.. py:module:: requests.adapters

adapters
========

.. py:class:: HTTPAdapter()

    .. code-block:: py

        adapter = HTTPAdapter(
            pool_connections=100,
            pool_maxsoze=100,
        )
        session.mount('htt://', adapter)
        