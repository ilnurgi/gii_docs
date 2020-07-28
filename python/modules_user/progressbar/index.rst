.. title:: python progressbar

.. meta::
    :description:
        Справочная информация по python библиотеке progressbar.
    :keywords:
        python progressbar

.. py:module:: progressbar

progressbar
===========

.. code-block:: sh

    pip install progressbar

.. code-block:: py

    from time import sleep

    from progressbar.bar import IncrementalBar

    steps = list(range(10))

    bar = IncrementalBar('Осталось шагов:', max=len(steps))

    for _ in steps:
        bar.next()
        sleep(1)
    bar.finish()
