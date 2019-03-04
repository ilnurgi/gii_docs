md5
===

.. code-block:: sh

    npm install md5

.. code-block:: js

    const fs = require('fs');
    const md5 = require('md5');

    const md5Hash = md5(fs.readFileSync(file_path));