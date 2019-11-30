.. title:: js string

.. meta::
    :description:
        Описание javascript объекта string
    :keywords:
        js string

String
======

.. js:class:: String()

    Строки

    Наследник :js:class:`Object`

    .. code-block:: js

        s = new String('test');
        string = 'ilnurgi';

    .. code-block:: js

        s += 's';

        'ilnurgi' + 123;
        // 'ilnurgi123'

        '12'/2 + 1;
        // 7

        'day' * 2;
        // NaN

        'a' < 'b';
        // true

        'c' < 'b';
        // false

        'bra' / 2;
        // NaN


    .. js:function:: length

        .. code-block:: js

            'ilnurgi'.length;
            // 7


    .. js:function:: charAt(index)

        Возвращает символ по индексу

        .. code-block:: js

            'ilnurgi'.charAt(2);
            // 'n'

            'ilnurgi'.charAt(200);
            // ''

            'ilnurgi'.charAt(-1);
            // ''


    .. js:function:: charCodeAt(index)

        Возвращает число, код символа из строки

        .. code-block:: js

            '!'.charCodeAt(0);
            // 33


    .. js:function:: codePointAt(index)

        Возвращает неотрицательное целое число - кодовый пнкт символа.

        .. note:: EcmaScript6

        .. code-block:: js

            '\uD83D\uDE91'.codePointAt(1);
            // 56977

            '\u{1F691}'.codePointAt(1);
            // 56977

            'hello'.codePointAt(2);
            // 1080


    .. js:function:: concat(string..)

        Возвращает новую строку, соединенную с указанными

        .. code-block:: js

            "C".concat("a", "t");
            // "Cat"


    .. js:function:: endsWith(string, index)

        Проверяет, заканчивается ли строка на указанную

        .. note:: EcmaScript6

        .. code-block:: js

            "ilnurgi".endsWith("il");
            // false


    .. js:function:: fromCharCode(char...)

        Статический метод, возвращает строку из последовательности чисел

        .. code-block:: js

            String.fromCharCode(33);
            // '!'

            String.fromCharCode(104, 101, 108, 108, 111);
            // "hello"


    .. js:function:: fromCodePoint(number1, ...)

        Возвращает строку по кодовым пунктам

        .. note:: EcmaScript6

        .. code-block:: js

            String.fromCodePoint(0x61, 0x62, 0x63);
            // 'abc'


    .. js:function:: includes(string, index=0)

        Проверяет наличие подстроки в строке

        .. note:: EcmaScript6

        .. code-block:: js

            "ilnurgi".includes('il');
            // true


    .. js:function:: indexOf(searchString, [start_pos])

        Возвращает число, индекс вхождения подстроки в строку.

        Возвращает -1 если не найдено

        .. code-block:: js

            'строка'.indexOf("ока");
            // 3


    .. js:function:: lastIndexOf(searchString, [start_pos])

        Возвращает число, индекс вхождения подстроки в строку с конца

        .. code-block:: js

            'строка'.lastIndexOf("ока");
            // 3


    .. js:function:: localeCompare(str)

        Сравнивает строки с учетом порядка следования символов национальных алфавитов

        Возвращает 0 если строки равны
        Возвращает отрицательное число если аргумент меньше


    .. js:function:: match(regexp)

        Возвращает массив найденных вхождений по регулярке

        .. code-block:: js

            "kj5k3".match(/\d/);
            // ["5"]

            "kj5k3".match(/\d/g);
            // ["5", "3"]


    .. js:function:: normalize()

        Возвращает нормализованную строку, по умолчанию NFC.

        .. note:: Нормализованная версия не используется для отображение, только для различных операции: сравнение и т.п.

        .. versionadded:::: EcmaScript6


    .. js:function:: padEnd(target_length [, pad_string=' '])

        Возвращает строку, расширенную до указанной длины, если она короткая, заполенную указанным символам справа

        .. code-block:: js

            let s = 'ilnurgi'
            s.padStart(10)
            // 'ilnurgi   '


    .. js:function:: padStart(target_length [, pad_string=' '])

        Возвращает строку, расширенную до указанной длины, если она короткая, заполенную указанным символам слева

        .. code-block:: js

            let s = 'ilnurgi'
            s.padStart(10)
            // '   ilnurgi'


    .. js:function:: repeat(count)

        Возвращает строку, содержащую указанное количество копии

        .. versionadded:::: EcmaScript6

        .. code-block:: js

            "a".repeat(5);
            // "aaaaa"


    .. js:function:: replace(searchValue, replaceValue)

        Возвращает новую строку, заменяя в исходной указанные значения

        .. code-block:: js

            "mother_in_low".replace("_", "-");
            // "mother-in-low"

            "mother_in_low".replace("_", function(c){});

            "(777)888-2323".replace(/\((\d{3})\)/g, "$1-");
            // "111-888-2323"


    .. js:function:: search(regexp)

        Возвращает число, позицию первого символа соответсвия

        В отличие от :py:meth:`String.indexOf`
        работает только с регулярными выражениями


    .. js:function:: slice(start, [end])

        Возвращает срез строки

        .. code-block:: js

            'stringify'.substring(0, 1);
            // 's'

            'stringify'.substring(3);
            // 'ingify'

            'stringify'.substring(-5);
            // 'ngify'


    .. js:function:: split(separator, limit)

        Возаращает массив строк, полученная путем разбиения исходной

        .. code-block:: js

            "12345".split("", 3);
            // ["1", "2", "3"]

            "last, first ,middle".split(/\s*,\s*/);
            // ["last", "first", "middle"]


    .. js:function:: startsWith(string, index=0)

        Проверяет, начинается ли строка с указанной строки

        .. note:: EcmaScript6

        .. code-block:: js

            "ilnurgi".startsWith("il");
            // true


    .. js:function:: substr(start[, length])

        Срез строки с позиции `start`, количество `length` символов

        .. code-block:: js

            'stringify'.substr(2, 4);
            // 'ring'


    .. js:function:: substring(start[, end])

        Возвращает срез строки

        В отличие от :py:meth:`String.slice`
        отрицательные значение приравниваются к нулю.

        .. code-block:: js

            'stringify'.substring(0, 1);
            // 's'

            'stringify'.substring(2);
            // 'ringify'


    .. js:function:: toLocalLowerCase()

        Возвращает строку, приведенную к нижнему регистру в соответсвйи с локалью


    .. js:function:: toLocalUpperCase()

        Возвращает строку, приведенную к верхнему регистру в соответсвйи с локалью


    .. js:function:: toLowerCase()

        Возвращает строку, приведенную к нижнему регистру


    .. js:function:: toUpperCase()

        Возвращает строку, приведенную к верхнему регистру


    .. js:function:: trim()

        Возвращает копию строки, с удаленными пробелами вначале и в конце

        .. code-block:: js

            '   ilnurgi   '.trim() === 'ilnurgi'


    .. js:function:: trimEnd()

        Возвращает копию строки, с удаленными пробелами в конце

        .. code-block:: js

            '   ilnurgi   '.trimEnd() === '   ilnurgi'


    .. js:function:: trimStart()

        Возвращает копию строки, с удаленными пробелами в начале

        .. code-block:: js

            '   ilnurgi   '.trimStart() === 'ilnurgi   '


Интерполяция
------------

.. code-block:: js

    var str = "My first name is " + "ilnur" + " and last name " + "ilnur" + "gii"

.. note:: EcmaScript6

    .. code-block:: js

        let name = "ilnur";
        let last_nme = "gii";
        let str = `My first name is ${name} and last name ${name + last_name}`


Многострочные строки
--------------------

.. code-block:: js

    var multiline_str = "1\n2";

.. note:: EcmaScript6

    .. code-block:: js

        let multiline_str = `1
        2`;
