socket.io
=========

.. code-block:: sh

    npm install socket.io

.. code-block:: js

    const app = require('express')();
    const server = require('http').Server(app);
    const io = require('socket.io')(server);

    io.on('connection', function(socket){
        socket.emit('news', {hello: 'world'});
        socket.on('my other event', function(data){
            console.log('hello world');
        });
    });