.. js:module:: express

express
=======

.. code-block:: sh

    npm install express

.. code-block:: js

    const express = require('express')
    const cookieParse = require('cookie-parser')

    const server = express()

    server.use(express.urlencoded({
        extended: true
    }))
    server.use(cookieParse());

    server.get('/', (req, resp) => {
        resp.sendFile('index.html')
        req.cookie
        // { username: 'ilnurgi'}
    })
    server.listen(8000)

.. code-block:: js

    // index.js

    var express = require('express');
    var router = express.Router();

    router.get('/', function(req, res, next){
        res.render('index', {'title': 'hello world'});
    });

    router.post('/', function(req, res, next){
        const city = req.body.city;
    });

    module.exports = router;

express()
---------

.. js:function:: express()

    Возвращает объект сервера :js:class:`Server`

    .. code-block:: js

        const app = express();

    .. js:function:: urlencoded(params)

        * params - объект, параметры метода

            * extended - булево

static()
--------

.. js:function:: static()

    .. code-block:: js

        server.use(express.static(__dirname))


Server
------

.. js:class:: Server()

    Объект сервера


    .. js:function:: get(route, callback)

        Задает обработчик для маршрута/урла. В обработчик приед :js:class:`Request` и :js:class:`Response`

        .. code-block:: js

            app.get('/', (req, res) => {
                res.sendFile('index.html');
            });

            // app.get('/:page?', (req, res) => {
            app.get('/:page', (req, res) => {
                var page = req.params.page;
                res.redirect('/');
            });

        .. code-block:: js

            let context = {
                content: "Hello World"
            };

            app.get('/', (req, res) => {
                res.render('index', context);
            });


    .. js:function:: listen(port[, host[, callback]])

        Запускает сервер по указанным параметрам

        ..  code-block:: js

            app.listen(8000);
            app.listen(8000, () => console.log("Server started"));


    .. js:function:: post(url, handler)

        .. code-block:: js

            server.post('/', (req, res) => {
                //
            })


    .. js:function:: route()

        .. code-block:: js

            app.route('new')
                .get((req, resp) => {})
                .post((req, resp) => {} );


    .. js:function:: set(key, value)

        Задает значения для параметров

        .. code-block:: js

            // задаем шаблонизатор для рендеринга
            app.set("view engine", "ejs");
            app.set("view engine", "jade");


    .. js:function:: use()

        Мидлваре

        .. code-block:: js

            app.use(function(req, res, next){
                next();
            });

        .. code-block:: js

            import apiRouter from './apiRouter';

            app.use(logger(dev));
            app.use(cookieParser());
            app.use(bodyParser.urlencoded({extended: true}));
            app.use(express.static(static_path));
            app.use('/static', express.static(static_path));
            app.use('/api', apiRouter);



Router
------

.. js:class:: Router()

    .. code-block:: js

        const router = express.Router();

    .. js:function:: get(url, callback)

        .. code-block:: js

            router.get('/', (req, res) => {
                res.send("Hello World");
            });

            router.get('/books/:bookId', (req, res) =>{
                // req.params.bookId
            });


Request
-------

.. js:class:: Request()

    Запрос на сервер

    .. js::attribute:: headers

        Заголовки запроса

        .. code-block:: js

            req.headers
            {
                host: '',
                cookie: ''
            }


    .. js:attribute:: hostname

        .. code-block:: js

            req.hostname
            // /

            
Response
--------

.. js:class:: Response()

    Ответ сервера

    .. js:function:: locals

        Локальные переменные объекта

        .. code-block:: js

            res.locals.usernmae = req.cookies.username

            
    .. js:function:: cookie(key, value)

        Устанавливает куки в отпвет
        
        ..code-block:: js

            res.cookie('username', 'ilnurgi')

    .. js:function:: redirect(url)

        Редирект

        .. code-block:: js

            res.redirect('/')
            // редирект на страницу откуда пришли
            res.redirect('back')

    .. js:function:: sendFile()

        .. code-block:: js

            res.sendFile('./index.html', {
                root: __dirname
            })

    .. js:function:: setHeader(key, value)

        Устанавливает заголовки ответа

        .. code-block:: js

            res.setHeader('Set-Cookie', ['username=ilnurgi'])


