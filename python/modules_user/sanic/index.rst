.. title:: python sanic

.. meta::
    :description:
        Справочная информация по python библиотеке sanic.
    :keywords:
        python sanic

.. py:module:: sanic

sanic
=====

`github <https://github.com/huge-success/sanic>`_

.. code-block:: ssh

    pip install sanic

.. code-block:: py

    from sanic import Sanic
    from sanic.response import json

    app = Sanic()

    @app.route('/')
    async def test(request):
        return json({'hello': 'world'})

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8000)
