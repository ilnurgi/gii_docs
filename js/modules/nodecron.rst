.. title:: js node-cron

.. meta::
    :description:
        Описание js модуля node-cron.
    :keywords:
        js node-cron

node-cron
=========

.. code-block:: sh

    npm install node-cron


.. code-block:: js

    const cron = require('node-cron');

    cron.schedule('* * * * *', () => {
        console.log('every minute task');
    })
