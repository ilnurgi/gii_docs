http
====

Вебсервер

.. code-block:: js

    const http = require('http');


createServer
------------

.. js:function:: createServer(callback)

    Возвращает объект сервера :js:class:`Server`

    .. code-block:: js

        const server = http.createServer((request, response) => {
            // request.url
            //
        });


Server
------

.. js:class:: Server()

    Сервер


    .. js:function:: listen(port)

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

    .. js:attribute:: url


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

            response.writeHead(status, {'Content-type': 'application-json'})