nunjuscks
=========

.. code-block:: sh

    npm install numjuscks

.. code-block:: js

    const app = express();
    const nunjucks = require('nunjucks');

    nunjucks.configure('path_to_pages', {
        autoescape: true,
        express: app,
    });

    app.get('/', (req, resp) => {
        resp.render('index.html', {
            date: new Date(),
        });
    });

.. code-block:: html

    <h>{{ date }}</h>