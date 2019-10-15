.. title:: axios

.. meta::
    :description: 
        Описание библиотеки axios для осуществления http запросов.
    :keywords: 
        axios

axios
=====

https://github.com/axios/axios

.. code-block:: sh

    npm install axios

.. code-block:: js

    const axios = require('axios');

    axios.get('url').then((response) => {
        log(response.data);
        // html data
    });
    