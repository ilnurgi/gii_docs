.. title:: js array

.. meta::
    :description:
        Описание javascript объекта Array.
    :keywords:
        js array

Array
=====

Array()
-------

.. js:class:: Array()

    Массив

    Наследник :js:class:`Object`

    .. code-block:: js

        var arr = new Array();

        var arr = new Array('hey', 'you');

        var arr = new Array(3);

        var arr = [];

    .. code-block:: js

        var array = [];

        var cities = ['moscow', 'kazan'];
        cities.length;
        // 2

        cities[0];
        // 'moscow'

        cities[3] = 'abakan';
        cities.length;
        // 4

        cities;
        // ['moscow', 'kazan', '', 'abakan']

        cities.length = 2;
        cities;
        // ['moscow', 'kazan']

        cities['city'] = 45;
        cities.length;
        // 2

    .. code-block:: js

        var a = [];
        a[5] = 5;
        for (var x in a){
            // выведет только 5
        }
        for (var i=0; i<a.length; i++){
            // выведет все 5 элементов
        }

    .. code-block:: js

        let [a, b, c] = [1, 2, 3];

        let [a, , b] = [1, 2, 3];
        console.log(a, b);
        // 1, 3

        let [a, ...b] = [1, 2, 3, 4];
        console.log(b);
        // [2, 3, 4]

        let [a, , , ...b] = [1, 2, 3, 4, 5, 6];
        console.log(b);
        // [4, 5, 6]

        let newArray = [...oldArray, newValue];
        let uniqFruits = [...new Set(fruitsList)];

    .. code-block:: js

        // перемешать массив
        [1, 2, 3, 4, 5, 6, 7, 8, 9].sort(function() {
            return Math.random() - 0.5;
        });
        // [8, 2, 9, 1, 3, 6, 5 ,7, 2]

    .. py:attribute:: length

        Возвращает число, количество элементов в массиве

        .. code-block:: js

            ['moscow', 'kazan'].length;
            // 2


    .. py:method:: concat(item...)

        Возвращает новый массив, расширенный значениями из аргумента

        Ели аргументом является массив, то добавляются только те элменты
        которых нет в исходном массиве

        .. code-block:: js

            var a = [1, 2, 3];

            a.concat([4, 5], 'end');
            // [1, 2, 3, 4, 5, 'end']

            a.concat([4, 5]);
            // [1, 2, 3, 4, 5]

            a.concat([4, 5], [6, 7]);
            // [1, 2, 3, 4, 5, 6, 7]

            [].concat(...[1, [2, 5], [6, 7], 9])
            // [1, 2, 5, 6, 7, 9]


    .. py:method:: copyWithin(targetIndex, startIndex, endIndex)

        Копирует последовательность значений массива в другое место этого массива

        .. versionadded:: EcmaScript6

        .. code-block:: js

            let arr1 = [1, 2, 3, 4, 5];
            arr1.copyWithin(1, 2, 4);
            arr1;
            // 1, 3, 4, 4, 5

            let arr2 = [1, 2, 3, 4, 5];
            arr2.copyWithin(0, 1);
            arr2;
            // 2, 3, 4, 5, 5

            let arr3 = [1, 2, 3, 4, 5];
            arr3.copyWithin(1, -2);
            arr3;
            // 1, 4, 5, 4, 5

            let arr4 = [1, 2, 3, 4, 5];
            arr4.copyWithin(1, -2, -1);
            arr4;
            // 1, 4, 3, 4, 5


    .. py:method:: entries()

        Возвращает итерируемый объект, содержащий массив пары ключ/значение, для каждого индекса массива.

        .. versionadded:: EcmaScript6


    .. py:method:: every(callback[, this])

        Возвращает булево, соответсвие всех элементов массива условию обработчика.

        .. versionadded:: ECMAScript5

        .. code-block:: js

            [1, 2, 3].every(function(item, index, array){
                return x < 5
            });
            // true

            [1, 2, 3].every(function(item, index, array){
                return x < 3
            });
            // false


    .. py:method:: fill(value, startIndex, endIndex)

        Заменяет все элементы массива в казанном промежутке указанным значением.

        .. note:: EcmaScript6

        .. code-block:: js

            [1, 2, 3, 4].fill(5);
            // [5, 5, 5, 5]

            [1, 2, 3, 4].fill(5, 1, 2);
            // [1, 5, 3, 4]

            [1, 2, 3, 4].fill(5, 1, 3);
            // [1, 5, 5, 4]

            [1, 2, 3, 4].fill(5, -3, 2);
            // [1, 5, 3, 4]

            [1, 2, 3, 4].fill(5, 0, -2);
            // [5, 5, 3, 4]


    .. py:method:: filter(callback[, filter])

        Возвращает массив элементов, удовлетворяющих требованиям обработчика

        .. versionadded:: ECMAScript5

        .. code-block:: js

            [1,2,3].filter(function(item, index, array) {
                return item > 1;
            });
            // [2, 3]


    .. py:method:: find(testingFunc, this)

        Возвращает элемент массива, который удовлетворяет условиям функции проверки

        .. versionadded:: ECMAScript5

        .. code-block:: js

            [11, 12, 13].find(function(value, index, array){
                if (value == this){
                    return true;
                }
            }, 12);
            // 12


    .. py:method:: findIndex(testingFunc, this)

        Возвращает индекс элемента массива удовлетворяющего условию

        .. versionadded:: EcmaScript6

        .. code-block:: js

            [11, 12, 13].find(function(value, index, array){
                if (value == this){
                    return true;
                }
            }, 12);
            // 1


    ..py:method:: flat(dim)

        .. versionadded:: ES2019

        Преобразует многомерный массив в одномерный на заданную максимальную глубину

        .. code-block:: py

            [
                [1, 2, 3],
                [4, 5, 6],
                [7, [8, 9]],
            ].flat(2) === [1, 2, 3, 4, 5, 6, 7, 8, 9]


    ..py:method:: flatMap()

        .. versionadded:: ES2019

        .. code-block:: py

            const texts = ["Hello,", "today I", "will", "use FlatMap"];

            texts.map(text => text.split(' ')) === ['Hello', ['today', 'I'], 'will', ['use', 'FlatMap']];

            texts.flatMap(text => text.split(' ')) === ['Hello', 'today', 'I', 'will', 'use', 'FlatMap'];


    .. py:method:: forEach(callback[, this])

        Вызывает функцию-обработчик для каждого элемента массива

        .. versionadded:: ECMAScript5

        .. code-block:: js

            [1, 2, 3].forEach(function(item, index, array){
                ...
            });


    .. py:method:: from(iterable, function, this)

        Позволяет получить массив из какого то объекта,
        например из живого массива элементов дом дерева.

        .. note:: ECMAScript6

        .. code-block:: js

            Array.from("1, 2, 3", function(item){
                return this.number * item;
            }, {number: 10});
            // [10, 20, 30]

            const liveArraySections = document.getElementsByTagName('section');
            // liveArraySections.forEach не будет работать, т.к. живая коллекция
            Array.from(liveArraySections).forEach(callback);


    .. py:method:: join(separator=',')

        Возвращает строку,
        полученную преобразованием всех элементов массива в строки и
        объединенные через разделитель

        .. versionadded:: ECMAScript5

        .. code-block:: js

            [1,2,3].join('');
            // '123'


    .. py:method:: includes(value, fromIndex=0)

        Возвращает булево, есть ли объект в массиве

        .. code-block:: js

            [1, 2, 3].includes(2);
            // true

            ['cat', 'dog', 'bat'].includes('cat');
            // true

            ['cat', 'dog', 'bat'].includes('at');
            // false


    .. py:method:: indexOf(value, pos=0)

        Возвращает число, индекс элемента в массиве

        .. versionadded:: ECMAScript5

        .. code-block:: js

            ['a','b','c'].indexOf('b');
            // 1

            ['a','b','c'].indexOf('d');
            // -1

            ['a','b','c'].indexOf('a', 1);
            // -1


    .. py:method:: keys()

        Возвращает итерируемый объект, содержащий ключи для всех идексов массива.

        .. versionadded:: EcmaScript6


    .. py:method:: lastIndexOf(значение[, int pos=array.length])

        Возвращает число, позиция элемента в массиве в обратном порядке

        .. versionadded:: ECMAScript5


    .. py:method:: map(callback[, this])

        Возвращает массив, вычисленный по функции-обработчику

        .. versionadded:: ECMAScript5

        .. code-block:: js

            [1, 2, 3].map(function(item, index, array) {
                return item * item;
            });
            // [1, 4, 9]


    .. py:method:: of(values...)

        Создает массив из 1 значения

        .. note:: EcmaScript6

        .. code-block:: js

            Array(2);
            // []

            Array.of(2);
            // [2]


    .. py:method:: pop()

        Возвращает последний элемент и удаляет его и массива

        .. versionadded:: ECMAScript5

        .. code-block:: js

            var c = [1,2,3];
            c.pop();
            // 3

            c;
            // [1,2]


    .. py:method:: push(item...)

         Добавляет объект в конец массива и возвращает количесвто элементов в массиве

        .. code-block:: js

            var c = [1, 2, 3];
            c.push(4);
            c;
            // [1, 2, 3, 4]

            c.push(5, 6, 7);
            c;
            // [1, 2, 3, 4, 5, 6, 7]

        .. code-block:: js

            // копирование значений из одного массива в другой
            var array1 = [2, 3, 4];
            var array2 = [1];
            Array.prototype.push.apply(array2, array1);
            // [1, 2, 3, 4]

        .. note:: EcmaScript6

            .. code-block:: js

                // копирование значений из одного массива в другой
                var array1 = [2, 3, 4];
                var array2 = [1];
                array2.push(...array1)
                // [1, 2, 3, 4]


    .. py:method:: reduce(callback[, int start=0])

        Вычисляет значение на основе элементов данного массива, свертка массива

        .. versionadded:: ECMAScript5

        .. code-block:: js

            [1,2,3].reduce(function(a, b){
                return a + b;
            });
            // 6


    .. py:method:: reduceRight(callback[, int start=0])

        Вычисляет значение на основе элементов данного массива,
        спарва налево, свертка массива

        .. versionadded:: ECMAScript5


    .. py:method:: reverse()

        Возвращает развернутый в обратныом порядке массив

        .. code-block:: js

            var a = [1, 2, 3];
            a.reverse();
            // [3, 2, 1]


    .. py:method:: shift()

        Возвращает первый элемент массива, и удалеят его из массива

        .. code-block:: js

            var a = [1, [2, 3], 4];
            var b = a.shift();
            // 1

            a;
            // [[2, 3], 4]


    .. py:method:: slice(start, end)

        Возвращает фрагмент массива

        .. code-block:: js

            [1, 2, 3, 4, 5].slice(0, 3);
            // [1, 2, 3]

            [1, 2, 3, 4, 5].slice(3);
            // [4, 5]

            [1, 2, 3, 4, 5].slice(1, -1);
            // [2, 3, 4]

            [1, 2, 3, 4, 5].slice(-3, -2);
            // [3]


    .. py:method:: some(callback[, this])

        Проверяет, возвращает ли предикат значение true хотя бы для одного элемента массива

        .. versionadded:: ECMAScript5

        .. code-block:: js

            [1,2,3].some(function(item, index, array) {
                return x > 5;
            })
            // => false: нет эле­мен­тов > 5

            [1,2,3].some(function(item, index, array) {
                return x > 2;
            })
            // => true: не­ко­то­рые > 3

            [].some(function(item, index, array) {
                return true;
            });
            // => false: все­гда false для []


    .. py:method:: sort([comparator])

        Сортирует массив, принимает функцию сравнения,
        которая может вернуть -1, 0, 1

        .. code-block:: js

            var a = [1, 2, 15];
            a.sort();
            a;
            // [1, 15, 2]

            a.sort(func(a, b){});


    .. py:method:: splice(start, deleteCount, item...)

        Удаляет указанный срез и возвращает их,
        вставляя в исходный массив указанные элементы массива

        .. code-block:: js

            var c = [1, 2, 3, 4, 5];

            c.splice(1,2);
            // [2, 3]

            c;
            // [1, 4, 5];

            c.splice(1, 2, 33, 44);
            // [4, 5]

            c;
            // [1, 33, 44]


    .. py:method:: unshift(item...)

        Добавляет в начало массива элементы и возвращает длину массива

        .. code-block:: js

            var a = [];
            a.unshift(1);
            a;
            // [1]

            a.unshift(-1, 0);
            a;
            // [-1, 0, 1]


    .. py:method:: values()

        Возвращает итерируемый объект, содержащий значения элементов массива.

        .. versionadded:: EcmaScript6


Итератор
--------

.. code-block:: js

    let mArray = [10, 20, 30];
    let mIterator = mArray[Symbol.iterator]();
    mIterator.next();
    // {value: 10, done: false}


ArrayBuffer()
-------------

.. py:class:: ArrayBuffer(size)


    .. versionadded:: EcmaScript6

    Буферный массив - это коллекция 8 битовых блоков в памяти.

    Размер определяется при его создании и не может увеличиваться динамический.

    Буферные массивы могут хранить только числа.

    В момент создания буферного массива все его блоки инициализируются нулями.

    Для чтения и записи данных в буфер используют :py:class:`DataView`

    .. code-block:: js

        let buffer = new ArrayBuffer(80);


    .. py:attribute:: byteLength

        Длина в байтах последовательности


ArrayTyped()
------------

.. py:class:: ArrayTyped(size)

    .. note:: EcmaScript6

    .. code-block:: js

        let buffer = new ArrayBuffer(80);
        let view = new DataView(buffer);
        view.setInt32(8, 22, false);
        view.getInt32(8, false);
        // 22

    .. py:method:: setInt8(offset, value, be)
    .. py:method:: setInt16(offset, value, be)
    .. py:method:: setInt32(offset, value, be)

        Использует 8/16/32 бит для хранения числа, принимает целое число со знаком

        * `offset` - количесвто байтов, которое следует отступить от начала массива перед чтением/записью числа.
        * `value` - записываемое число
        * `be` - порядок записи байтов байтов числа, false - старшие байты будут записаны первыми.


    .. py:method:: setUint8(offset, value, be)
    .. py:method:: setUint16(offset, value, be)
    .. py:method:: setUint32(offset, value, be)

        Использует 8/16/32 бит для хранения числа, принимает целое число без знака


    .. py:method:: setFloat32(offset, value, be)
    .. py:method:: setFloat64(offset, value, be)

        Использует 32/64 бит для хранения числа, принимает вещественное число со знаком


    .. py:method:: getInt8(offset, be)
    .. py:method:: getInt16(offset, be)
    .. py:method:: getInt32(offset, be)

        Читает 8/16/32 бит и возвращает целое число со знаком


    .. py:method:: getUint8(offset, be)
    .. py:method:: getUint16(offset, be)
    .. py:method:: getUint32(offset, be)

        Читает 8/16/32 бит и возвращает целое число без знака

    .. py:method:: getFloat32(offset, be)
    .. py:method:: getFloat64(offset, be)

        Читает 32/64 бит и возвращает вещественное число со знаком


Float32Array(), Float64Array()
------------------------------

.. py:class:: Float32Array(buffer)

    .. note:: EcmaScript6

.. py:class:: Float64Array(buffer)

    .. note:: EcmaScript6

    Буферный массив 64-битных вещественных чисел

    .. code-block:: js

        // создаем буферный массив на 640 бит, 80 * 8
        let buffer = new ArrayBuffer(80);

        // создаем типизированный буфер 64 битных чисел
        // в буфере можно хранить не более 10 числе, 640/64
        let typed_array = new Float64Array(buffer);
        typed_array[4] = 11;

        typed_array.length;
        // 10

        typed_array[4];
        // 11


Int8Array(), Int16Array(), Int32Array()
---------------------------------------

Буферный массив для 8/16/32 битных чисел со знаком

.. py:class:: Int8Array(buffer)

    .. note:: EcmaScript6


.. py:class:: Int16Array(buffer)

    .. note:: EcmaScript6


.. py:class:: Int32Array(buffer)

    .. note:: EcmaScript6


Uint8Array(), Uint16Array(), Uint32Array()
------------------------------------------

Буферный массив для 8/16/32 битных чисел без знака

.. py:class:: Uint8Array(buffer)

    .. note:: EcmaScript6


.. py:class:: Uint16Array(buffer)

    .. note:: EcmaScript6


.. py:class:: Uint32Array(buffer)

    .. note:: EcmaScript6


