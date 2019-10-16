.. title:: js array

.. meta::
    :description: 
        Описание массивов, array, в языке программирования java script
    :keywords: 
        js array

Function
========

.. code-block:: js

    // эта функция будет создана в самом начале при чтении скрипта
    function name(){}

    // эта функция будет создана тогда, когда интерпретаор до него дойдет
    var name = function(){}

    // arguments - массив всех принятых аргументов
    var average = function(x, y){
        log(arguments);
    }

    // параметры по умолчанию
    function some(x, y, z){
        x = x || 1;
        y = y || 2;
        z = z || 3;
    }

    // параметры по умолчанию в новой спецификации
    function some(x=1, y=2, z=3){};

    // передача параметров с распаковкой
    function some(a, b){}
    some(...[1, 4]);

    function some(a, b ...c){};

    // анонимная функция
    (function(){})();

    // стрелочная функция    
    // this, внутри стрелочной функции, не является ссылкой на функцию
    let circleArea = (pi, r) => {};
    let circleArea2 = (pi, r) => pi * r * r;
    let square = x => x * x;
    let log = () => console.log("Some text");
    let getPerson = () => ({ name: "ilnurgi" });
    (() => console.log("IIFE"))();

.. code-block:: js

    // асинхронная функция
    function func1(x){
        return new Promise(
            resolve => {
                setTimeout(
                    () => {
                        resolve(x);
                    }, 2000
                )
            }
        );
    }
    async function add1(x) {
        const a = await func1(20);
        const b = await func1(30);
        return x + a + b;
    }
    add1(10).then(
        v=> {
            console.log(v);
        }
    )

.. code-block:: js

    // замыкание
    var getAnswer = (function(){
        var answer = 42;

        return function inner(){
            // эта переменная замыкается
            return answer;
        };
    }());

    getAnswer();
    // 42


Function
--------

.. js:class:: Function(args, function_body)

    Функция/конструктор функции, которая возвращает функцию

    Наследник :js:class:`Object`

    .. code-block:: js

        var func = Function("x", "y", "return x + y;")
        var result = func(20, 10)
        // 30


    .. js:attribute:: __proto__

        Ссылка экземпляра на прототип


    .. js:attribute:: arguments

        Массив аргументов, переданных функции


    .. js:attribute:: caller

        Ссылка на функцию, вызвавшую данную функцию


    .. js:attribute:: length

        Число именованных аргументов, указанных при объявлении функции


    .. js:attribute:: name

        Название функции


    .. js:attribute:: prototype
    
        Ссылка функции на прототип


    .. py:method:: apply(thisArg, arguments)

        Вызывает функцию с подменой контекста

        .. code-block:: js

            functionName.apply(thisArg, param1, param2)


    .. py:method:: bind(context, ...arguments)

        Возвращает новую функцию,
        которая вызывает данную,
        как метод указанного объекта с указанными аргументами.

        Таким образом можно подменить контекст

        .. code-block:: js

            function f(){
                alert(1);
            };
            var g = f.bind("Context", 1, 2);
            // эквивалентно f.call("Context", 1, 2);

        .. code-block:: js

            // карирование, фиксирование аргументов
            function mull(a, b){
                return a * b;
            }
            var double = mul.bind(null, 2)
            double(3);
            // mul(2, 3) = 6


    .. py:method:: call(obj, argument1, ...)

        Вызывает функцию как метод указанного объекта


Генератор
---------

.. note:: EcmaScript6

Функция возвращает несколько значений по одному. 

.. code-block:: js

    function* generator_function(){

        yield 1;
        yield 2;
    }
    var generator = generator_function()
    generator.next().value
    // 1
    generator.next().value
    // 2

.. code-block:: js
    
    // генератор с передачей параметра в yield
    function* generator_function(){
        var a = yield 12;
        var b = yield a + 1;
    }
    var generator = generator_function()
    generator.next().value
    // 12
    generator.next(5).value
    // 6

.. code-block:: js
    
    // досрочное завершение генератора
    function* generator_function(){
        var a = yield 12;
        var b = yield a + 1;
    }
    var generator = generator_function()
    generator.next().value
    // 12
    generator.return(5).value
    // 5

.. code-block:: js
    
    // вызов исключении в генераторе
    function* generator_function(){
        try {
            yield 1;
        } catch(e) {
            console.log("1st exception");
        }
        try {
            yield 2;
        } catch(e) {
            console.log("2st exception");
        }
    }
    var generator = generator_function()
    generator.next().value
    generator.throw("exception string").value
