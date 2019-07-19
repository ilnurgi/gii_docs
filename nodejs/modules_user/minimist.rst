minimist
========

Парсер аргументов процесса

.. code-block:: sh

    $ npm i minimist


.. code-block:: js

    const minimist = require('minimist')
    const argv = minimist(process.argv)

    // node script.js -x 3 -y 4 -n5 -abc --beep=boop foo bar baz
    { 
        _: [ 'foo', 'bar', 'baz' ],
        x: 3,
        y: 4,
        n: 5,
        a: true,
        b: true,
        c: true,
        beep: 'boop' 
    }