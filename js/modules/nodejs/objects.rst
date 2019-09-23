Объекты
=======

Buffer
------

.. code-block:: js

    buffer = new Buffer('Some string', 'utf-8');
    console.log(buffer);
    // <Buffer 33 40 ...>

    [].slice.call(buffer).forEach(function(octet) {
        process.stdout.write(octet.toString(2));
    });