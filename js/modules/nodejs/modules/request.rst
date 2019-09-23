request
=======

Полезные возможности модуля:

* автоматическая обработка JSON
* работа с учетом редиректов или без них через опцию followRedirects
* поддержка Basic Auth через опцию auth
* поддержка OAuth через опцию oauth
* поддержка прокси через опцию proxy
* поддержка cookies через опцию jar: true

.. code-block:: js

    const request = require('request');

    request('http://ilnurgi.ru', (err, response, body) => {
        //
    });

    requset({
        method: 'POST',
        uri: 'http://ilnurgi.ru',
        form: { k: 'v'}
    }, (err, resp, body) => {

    });