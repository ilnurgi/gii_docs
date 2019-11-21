.. title:: python aiohttp

.. meta::
    :description: 
        Справочная информация по python библиотеке aiohttp.
    :keywords: 
        python aiohttp

.. py:module:: aiohttp

aiohttp
=======

.. code-block:: py

    from aiohttp import web

    async def start_background_tasks(app):
        app['monitor'] = app.loop.create_task(monitor(app))

    async def cleanup_background_tasks(app):
        app['monitor'].cancel()
        await app['monitor']

    async def handle(request):
        pool = request.app['pool']
        power = int(request.match_info.get('power', 10))

        async with pool.asquire() as conn:
            async with conn.transaction():
                result = await conn.fetchval('select 2 ^ $1', power)
                return web.Response(text=f'2 ^ {power} = {result}')

    async def init_app():
        app = web.Application()
        app['pool'] = await asyncpg.create_pool(DSN)
        app.route.add_route('GET', '{power:\d+}', handle)
        return app

    if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        app = loop.run_until_complete(init_app())
        app.on_startup.append(start_background_tasks)
        app.on_cleanup.append(cleanup_background_tasks)
        web.run_app(app)