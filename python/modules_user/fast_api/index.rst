.. title:: python fast_api

.. meta::
    :description:
        Справочная информация по python библиотеке fast_api.
    :keywords:
        python fast_api

.. py:module:: fast_api

fast_api
========

`github <https://github.com/tiangolo/fastapi>`_

.. code-block:: ssh

    pip install fast_api

.. code-block:: py

    from fastapi import FastAPI

    app = FastAPI()


    @app.get("/")
    def read_root():
        return {"Hello": "World"}
