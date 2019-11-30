.. js:module:: net

net
===

.. code-block:: js

    const net = require('net');


createServer
------------

.. js:function:: createServer()

    Создает сервер

    .. code-block:: js

        const server = net.createServer(function(socket){
            socket.on('data', function(){
                socket.write(String(data));
            });
            socket.on('close', function(){
                //...
            });
        });

        server.listen(8000);


Socket
------

.. js:class:: Socket()

    .. js:attribute:: remoteAddress

        Удаленный адрес

    .. js:attribute:: remotePort

        Удаленный порт

