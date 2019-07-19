http
====

Вебсервер

.. code-block:: js

    const http = require('http');


createServer()
--------------

.. js:function:: createServer(callback)

    Возвращает объект сервера :js:class:`Server`

    .. code-block:: js

        const server = http.createServer((request, response) => {
            // request.url
            //
        });

get()
-----

.. js:function:: get(url, callback)

    Get запрос

    .. code-block:: js

        http.get('ilnurgi.ru', (res) => {
            res.statusCode;
        }).on('error', e => {
            e.message;
        });


request()
---------

.. js:function:: request(options, callback)

    POST запрос

    .. code-block:: js

        const options = {
            hostname: 'ilnurgi.ru',
            port: 80,
            path: '/statistic',
            method: 'POST'
        };

        const req = http.request(options, res => {
            res.statusCode;
            JSON.stringify(res.headers);
            res.setEncoding('utf8');
            res.on('data', chunk => {
                //
            });
        })
        req.on('error', e => {
            e.message;
        });
        req.write('data\n');
        req.end();


Server
------

.. js:class:: Server()

    Сервер


    .. js:function:: listen(port, host, callback)

        Указывает порт прослушки

        .. code-block:: js

            server.listen(8000);


    .. js:function:: on(event_name, callback)

        Регистрирует обработчик события

        * event_name - название события

            * request

        * callback - обработчик события, принимает два параметра :js:class:`Request`, :js:class:`Response`

        .. code-block:: js

            server.on('request', (req, res) => {
                res.write('Hello Worlf!\n');
                res.end();
            });

            server.on('request', (req, res) => {
                res.end(fs.reafFileSync(__dirname + '/index.html'));
            });

Request
-------

.. js:class:: Request()

    Объект запроса

    .. js:attribute:: headers

        .. code-block:: js

            request.headers
            {
                host: '127.0.0.1:3000',
                'user-agent': '',
                'accept-encoding': 'gzip',
                connection: 'close'
            }

    .. js:attribute:: method

        .. code-block:: js 

            request.method
            //  GET

    .. js:attribute:: url

        ..code-block:: js

            request.url
            // /


Response
--------

.. js:class:: Response()

    Объект ответа на запрос


    .. js:function:: end();

        Завершает обработку ответа на запрос

        .. code-block:: js

            res.end();
            res.end('Hello world');


    .. js:function:: write(body)

        Записывает ответ в тело ответа

        .. code-block:: js

            res.write('Hello World!\n');


    .. js:function:: writeHead()

        Добавляет в ответ заголовки

        .. code-block:: js

            response.writeHead(200, {'Content-type': 'application-json'})


            