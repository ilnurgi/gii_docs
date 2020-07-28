.. title:: python starlette

.. meta::
    :description:
        Справочная информация по python библиотеке starlette, асинхронный веб сервер.
    :keywords:
        python starlette

starlette
=========

`starlette <https://www.starlette.io/>`_

`github <https://github.com/encode/starlette>`_

.. code-block:: ssh

    pip install starlette

.. code-block:: py

    from starlette.applications import Starlette
    from starlette.responses import JSONResponse
    import uvicorn

    app = Starlette(debug=True)


    @app.route('/')
    async def homepage(request):
        return JSONResponse({'hello': 'world'})

    if __name__ == '__main__':
        uvicorn.run(app, host='0.0.0.0', port=8000)
