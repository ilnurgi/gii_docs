.. title:: js.fetch

.. meta::
    :description: js.fetch
    :keywords: js.fetch

fetch()
=======

.. js:function:: fetch(url, options)

    Запрос на сервер. 

    Возвращает :js:class:`Promise()`, в результат которого придет :js:class:`Response()`

    * options - объект с опциями

        * body – тело запроса: FormData, Blob, строка и т.п.

        * cache – default | no-store | reload | no-cache | force-cache | only-if-cached, указывает, как кешировать запрос.
        
        * credentials – omit | same-origin | include, указывает, пересылать ли куки и заголовки авторизации вместе с запросом.
        
        * headers – заголовки запроса (объект)

        * method – метод запроса
        
        * mode – same-origin | no-cors | cors, указывает, в каком режиме кросс-доменности предполагается делать запрос.

        * redirect – `follow` для обычного поведения при коде 30x (следовать редиректу) или `error` для интерпретации редиректа как ошибки.
    
    .. code-block:: js

        fetch(url, options)
            .then(function(response) {
                response.arrayBuffer();
                response.headers;
                response.status; // 200
                return response.json();
            })
            .then(function(user) {
                user.name; // ilnurgi
            })
            .catch(alert);