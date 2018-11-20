Worker - фоновый поток выполнения
=================================


.. js:class:: Worker(scriptUrl)


    .. js:attribute:: onerror
        
        Когда в сценарии, выполняемом в фоновом потоке, 
        возбуждается исключение и это исключение не обрабатывается обработчиком onerror объекта WorkerGlobalScope, 
        генерируется событие «error» в объекте Worker. 
        
        Обработчику этого события передается объект ErrorEvent. 
        
        Событие «error» не всплывает. 
        
        Если данный фоновый поток выполнения запущен другим фоновым потоком, 
        отмена события «error» предотвратит его передачу родительскому фоновому потоку. 
        
        Если объект Worker создан в главном потоке выполнения, 
        отмена события может предотвратить вывод сообщения в консоли JavaScript.


    .. js:attribute:: onmessage
        
        Когда сценарий, выполняемый в фоновом потоке, 
        вызовет свою глобальную функцию postMessage() (см. WorkerGlobalScope), 
        в объекте Worker будет сгенерировано событие «message». 
        
        Обработчику события будет передан объект MessageEvent, 
        свойство data которого будет содержать копию значения, 
        переданного сценарием из фонового потока выполнения методу postMessage().


    .. js:function:: postMessage(any message, [MessagePort[] ports])
        
        Отправляет сообщение message фоновому потоку выполнения, 
        котопый получит его в виде объекта MessageEvent, 
        в обработчике onmessage. 
        
        Аргумент message может быть простым значением, объектом или массивом, но не функцией. 
        
        Допускается передавать такие объекты клиентского JavaScript, 
        как ArrayBuffer, File, Blob и ImageData, но узлы, такие как Document и Element, передавать нельзя.
        
        Необязательный аргумент ports позволяет указать один или более прямых каналов связи с  объектом Worker. 
        
        Например, если имеются два объекта Worker, можно обеспечить прямое взаимодействие между ними, 
        передав их конструкторам концы соединения MessageChannel.


    .. js:function:: terminate()
        
        Останавливает фоновый поток выполнения и прерывает работу сценария в нем.

.. code-block:: js

    // worker.js
    onmessage = function(e) {
        setTimeout(() => {
            postMessage(e.data);
        }, 2000);
    };

.. code-block:: js

    // app.js

    var worker = new Worker('worker.js');
    worker.postMessage('Hello World');
    worker.addEventListener('message', (e) => {
        console.log(e.data);
    }, false);