events
======

События

.. code-block:: js

    const events = require('events');


EventEmitter
------------

.. js:class:: EventEmitter()

    .. code-block:: js

        const emitter = new events.EventEmitter();


    .. js:function:: addListener(event_name, callback)

        Устанавливает обработчик на событие


    .. js:function:: on(event_name, callback)

        Устанавливает обработчик на событие

        .. code-block:: js

            emitter.on('click', function(){});


    .. js:function:: once(event_name, callback)

        Устанавливает обработчик на событие, которое отработает только 1 раз


    .. js:function:: emmit(event_name)

        Генерация события

        .. code-block:: js

            emitter.emit('click');