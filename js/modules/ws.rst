.. title:: js ws

.. meta::
    :description:
        Описание js модуля ws.
    :keywords:
        js ws

node-cron
=========

.. code-block:: sh

    npm install ws


.. code-block:: js

    const WebSocket = require('ws');

    const ws = WebSocket(url);

    ws.on('open', () => {});
    ws.on('message', (data) => {});
    ws.on('close', () => {});

.. code-block:: js

    const WebSocket = require('ws');
    const wss = new WebSocket.Server({port: 8080});

    wss.on('connection', socket => {
        socket.on('message', data => {
            socket.send(data);
        });
    });

    console.log(`Listening on ws://localhost:8080`);
