stream
======

.. code-block:: js

    const stream = require('stream');


Readable
--------

.. js:class:: Readable()

    .. code-block:: js

        const stream = new stream.Readable();
        const data = ['1', '2', '3'];

        stream._read = function(){
            if (data.length){
                setTimeout(function(){
                    stream.push(data.shift());
                }, 200);
            } else {
                stream.push(null);
            }
        };

        stream.pipe(process.stdout);


Transform
---------

.. js:class:: Transform()

    .. code-block:: js

        const tr = new stream.Transform();

        tr._transform = function(chunk, enc, cb){
            var string = String(chunk);
            this.push(string);
            cb();
        };

        process.stdin
            .pipe(tr)
            .pipe(process.stdout);