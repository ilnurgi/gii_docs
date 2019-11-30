.. title:: cheerio.js

.. meta::
    :description: 
        Описание библиотеки cheerio.js для парсинга html документа.
    :keywords: 
        cheerio

cheerio
=======

https://cheerio.js.org/

.. code-block:: sh

    npm install cheerio

.. code-block:: js

    const cheerio = require('cheerio');

    const $ = cheerio.load(html_data);

    log($('#example').text());
    // some paragraph data