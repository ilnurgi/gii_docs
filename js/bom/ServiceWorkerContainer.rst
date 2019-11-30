.. title:: javascript serviceworker

.. meta::
    :description: 
        Описание объекта serviceworker, объектной модели браузера веб страницы.
    :keywords: 
        javascript serviceworker

.. py:module:: serviceworker

ServiceWorkerContainer
======================

.. code-block:: js

    // service-worke.js

    self.addEventListener("install", (event) => {
        let CACHE_NAME = 'ilnurgi-cache';
        let urlsToCache = [
            '/',
            '/styles/main.css',
            '/scripts/bundle.js',
        ];
        event.waitUntil(
            caches
                .open(CACHE_NAME)
                .then(cache => cache.addAll(urlsToCache));
        );
    });

    self.addEventListener('activate', (event) => {
        // sekf,skipWaiting();

        let cacheWhiteList = ['products-2'];
        event.waitUntil(
            caches
                .keys()
                .then(cacheNames => {
                    return Promise.all(
                        cacheNames.map(cacheName => {
                            if (cacheWhiteList.indexOf(cacheName) === -1){
                                return caches.delete(cacheName);
                            }
                        })
                    )
                })
        );
    })

    self.addEventListener('fetch', (event) => {
        event.respondWith(
            caches.open('products-v2')
                .then (cache => {
                    return cache.match(event.request).then (response => {
                        if (response) {
                            console.log('Cache hit! Fetching response from cache', event.request.url)
                            return response
                        }
                        fetch(event.request).then (response => {
                            cache.put(event.request, response.clone())
                            return response
                        })
                    })
                })
        )
    })


ServiceWorkerContainer()
------------------------

.. py:class:: ServiceWorkerContainer()

