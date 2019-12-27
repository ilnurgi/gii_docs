.. title:: python re

.. meta::
    :description:
        Справочная информация по python модулю re. Модуль для работы с регулярными выражениями в python.
    :keywords:
        python re, python регулярные выражения

.. py:module:: re

re
==

Модуль re в python предназначен для работы с регулярными выражениями в python.

Квантофикаторы
--------------

* **^** - привязка к началу строки или подстроки (зависит от флагов M и S)

    .. code-block:: py

        re.findall('^iln', 'ilnurgi')
        # ['iln']

        re.findall('^iln', ' ilnurgi')
        # []

* **$** - привязка к концу строки или подстроки (зависит от флагов M и S)

    .. code-block:: py

        re.findall('rgi^', 'ilnurgi')
        # ['rgi']

        re.findall('rgi^', ' ilnurgi ')
        # []

* **\\A** - привязка к началу строки или подстроки (не зависит от флагов)
* **\\z** - привязка к концу строки или подстроки (не зависит от флагов)
* **[]** - внутри указываются символы, которые могут встречаться
    * **[0-9]** - любая цифра
    * **[a-яА-ЯёЁ]** - любая русская буква
    * **[^3]** - не цифра 3
* **\\d** - любая цифра
* **\D** - НЕ цифра
* **\\w** - любая буква, цифра и символ подчеркивания
* **\\W** - НЕ буква, цифра и символ подчеркивания
* **\\s** - любой пробельный символ
* **\\S** - НЕ пробельный символ
* **{n}** - n вхождений символа в строку
* **{n, }** - n или более вхождений символа в строку
* **{n, m}** - не менее n и не более m вхождений символа в строку
* **\*** - 0 или более вхождение смвола в строку
* **+** - 1 или более вхождение символа в строку
* **?** - ни одного или 1 вхождение символа в строку
* **(n)|(m)** - n или m
* **(?P<tag>)** - тег для группы

    .. code-block:: py

        re.findall(
            '(?P<name>[a-z0-9.-]+)' # название ящика
            '@'
            '(?P<host>(?:[a-z0-9-]+\.)+[a-z]{2,6})', # домен
            "test@test.ru"
        )
        # [('test', 'test.ru')]

        r = re.search(
            '(?P<name>[a-z0-9.-]+)' # название ящика
            '@'
            '(?P<host>(?:[a-z0-9-]+\.)+[a-z]{2,6})', # домен
            "test@test.ru"
        )
        r.group("name")
        # 'test'
        # r.group("host")
        'test.ru'

* **(?P=tag)** - обращение к группе внутри регулярки
* **(?aiLmsux)** - флаги регулярного выражения
* **(?#...)** - коментарии, текст внутри скобок игнорируется
* **(?=...)** - положительный просмотр вперед

    .. code-block:: py

        # все слова, после которых есть запятая
        re.findall(
            r"\w+(?=[,])",
            "textl, text2, textЗ text4"
        )
        # ['text1', 'text2']

* **(?!...)** - отрицательный просотр вперед

    .. code-block:: py

        # все слова, после которых нет запятой
        re.findall(
            "[a-z]+[0-9] (?![,])",
            "textl, text2, textЗ text4"
        )
        # ['textЗ', 'text4']

* **(?<=...)** - положительный просмотр назад

    .. code-block:: py

        # все слова, перед которыми есть запятая с пробелм
        re.findall(
            "(?<=[,][ ])[a-z]+[0-9]",
            "textl, text2, textЗ text4"
        )
        # ['text2', 'text3']

* **(?<!...)** - отрицательный просотр назад

    .. code-block:: py

        # все слова, перед которыми есть пробел но нет запятой
        re.findall(
            "(?<![,]) ([a-z]+[0-9])",
            "textl, text2, textЗ text4"(        ))


        # ['text4']

* **(?(id или name) шаблон1|шаблон2)** - если группа с номером,
  или названием найдена,
  то должно выполняться условие из параметра шаблон1,
  в противном случае должно выпол­няться условие из параметра шаблон2.

    .. code-block:: py

        # все слова которые находятся внутри апострофа, либо после слова есть запятая
        re.findall(
            "(')?([a-z]+(0-9]) (?(1) '1,)",
            "textl 'text2' 'textЗ text4, text5"
        )
        # [("'", 'text2'), ('', 'text4')]

Все квантификаторы являются "жадными".

При поиске соответствия ищется самая длинная подстрока,
соответствующая шаблону, и не учитываются более короткие соответствия.

Чтобы ограничить жадность, необходимо после квантификатора указать символ **?**

.. code-block:: py

    s = "<b>Textl</b>Text2<b>Text3</b>"

    re.findall("<b>.*</b>", s)
    # ['<b>Textl</b>Text2<b>Toxt3</b>']

    re.findall("<b>.*?</b>", s)
    # ['<b>Textl</b>', '<b>Text3</b>']

.. code-block:: py

    re.findall('([a-z]+((st)|(xt)))', 'test text')
    # [('test', 'st', 'st', ''), ('text', 'xt', 'xt')]

    re.findall('([a-z]+(?:(?:st)|(?:xt)))', 'test text')
    # ['test', 'text']

    re.findall("<([a-z]+)>(.*?)</\1>", "<b>Textl</b>Text2<b>Text3</b>")
    # [('b', 'Text1'), ('b', 'Text3')]

    re.findall("<(?P<tag>[a-z]+)>(.*?)</(?P=tag))>", "<b>Textl</b>Text2<b>Text3</b>")
    # [('b', 'Text1'), ('b', 'Text3')]

.. code-block:: py

    def select(r, xs):
        """
        возвращает список, из найденных груп в исходном списке
        :param r: регулярка
        :param xs: список строк для парсинга
        """
        return [m.group() for m in (re.match(r, x) for x in xs) if m]

    l = ['aaa', 'aab', 'abb', 'bbb']

    select(r'a*', l)
    # ['aaa', 'aa', 'a', '']
    # "беру любое кол-во \"a\", даже нулевое!"

    select(r'a+', l)
    # ['aaa', 'aa', 'a']
    # "любое ненулевое кол-во, беру всё!"

    select(r'a*?', l)
    # ['', '', '', '']
    # "хочу 0+, беру минимум (т.е. не возьму ничего!)"

    select(r'a+?', l)
    # ['a', 'a', 'a']
    # "хочу 1+, беру минимум (т.е. одну штуку)"

    select(r'a?', l)
    # ['a', 'a', 'a', '']
    # "хочу (и беру) одну или ничего!"

    select(r'a{,2}', l)
    # ['aa', 'aa', 'a', '']
    # "хочу (и беру) до двух штук!"

    select(r'a{1,2}?', l)
    # ['a', 'a', 'a']
    # "хочу одну-две штуки, возьму минимум (одну)!"

    select(r'a{2}', l)
    # ['aa', 'aa']
    # "хочу (и беру) ровно две!"


.. code-block:: py

    s = 'aa,a ab aa aaa'

    re.findall(r'a+', s)
    # ['aa', 'a', 'a', 'aa', 'aaa']
    # "выбираю слова по подстроке, но могут быть неверные выборки!")

    re.findall(r'\Wa+\W', s)
    # [',a ', ' aa ']
    # "выбираю слова с небуквами по бокам и беру вместе с небуквами")

    re.findall(r'\sa+\s', s)
    # [' aa ']
    # "выбираю слова с пробелами по бокам и беру вместе с пробелами")

    re.findall(r'\ba+\b', s)
    # ['aa', 'a', 'aa', 'aaa']
    # "выбираю слова по границам слов, не беру сами границы!")

    re.findall(r'^a+', s)
    # ['aa']
    # "выбираю слово в начале строки")

    re.findall(r'a+$', s)
    # ['aaa']
    # "выбираю слово в конце строки")

.. code-block:: py

    s = 'a\nab\nabc'

    re.findall(r'^.+$', s)
    # []
    # "по-умолчанию точка не захватывает переводы строк, а ^ и $ обозначают границы всего текста:\n"

    re.findall(r'(?m)^.+$', s)
    # ['a', 'ab', 'abc']
    # "^ и $ теперь обрабатывают подстроки:\n"

    re.findall(r'(?s)^.+$', s)
    # ['a\nab\nabc']
    # "точка захватывает и переводы строк:\n"

    # "\A\Z всегда обозначают границы текста:"

    re.findall(r'\A.+\Z', s)
    # []

    re.findall(r'(?m)\A.+\Z', s)
    # []

    re.findall(r'(?s)\A.+\Z', s)
    # ['a\nab\nabc']


LOCALE
-------

.. py:attribute:: LOCALE
.. py:attribute:: L

    флаг, учитывать настройки локали


IGNORECASE
----------

.. py:attribute:: IGNORECASE
.. py:attribute:: I

    флаг, игнорировать регистр


MULTILINE
---------

.. py:attribute:: MULTILINE
.. py:attribute:: M

    флаг, поиск в строке, состоящей из нескольких подстрок


DOTALL
------

.. py:attribute:: DOTALL
.. py:attribute:: S

    флаг, метасимвол `точка` будет соответсвовать любому символу,
    включая символ перевода строки `\\n`


VERBOSE
-------

.. py:attribute:: VERBOSE
.. py:attribute:: X

    флаг, пробелы и символы перевода строк будут игнорированы


UNICODE
-------

.. py:attribute:: UNICODE
.. py:attribute:: U

    флаг, `\\w, \\W, \\b, \\B, \\d, \\D, \\s, \\S` будут соответствовать юникод символам
    (в 3 питоне флаг установлен по умолчанию)


ASCII
-------

.. py:attribute:: ASCII
.. py:attribute:: A

    флаг, `\\w, \\W, \\b, \\B, \\d, \\D, \\s, \\S` будут соответствовать обычным символам


compile()
---------

.. py:method:: compile(pattern, flags=0)

    Возвращает :py:class:`SRE_Pattern`, скомпилированный шаблон для парсинга.

    .. code-block:: py

        re.compile('\d+').findall('123ilnurgi123')
        # ['123', '123']

error()
-------

.. py:method:: error(msg, pattern=None, pos=None, lineno=None, colno=None)


escape()
--------

.. py:method:: escape(pattern)

    Возвращает строку, с экранированными специальными символами, полученной от пользователя.

    Эту строку в дальнейшем можно безопасно исполь­зовать внутри регулярного выражения.

    .. code-block:: py

        re.escape(r"[] () .*")
        # '\[\]\(\)\.\*''


findall()
---------

.. py:method:: findall(pattern, string, flags=0)

    Возвращает список найденных фрагментов

    .. code-block:: py

        re.findall(r"[0-9]+", "2007, 2008, 2009, 2010, 2011")
        # ['2007', '2008', '2009', '2010', '2011']


finditer()
----------

.. py:method:: finditer(pattern, string, flags=0)

    Возвращает итератор найденных фрагментов


fullmatch()
-----------

.. py:method:: fullmatch(pattern, string, flags=0)

    .. versionadded:: 3.4


match()
-------

.. py:method:: match(pattern, string, flags=0)

    Проверяет соотвествие с началом строки, если соответсвие найдено,
    возвращается :py:class:`Match` иначе None

    .. code-block:: py

        re.match('\d+', '123ilnurgi123')
        # <re.Match object; span=(0, 3), match='123'>


purge()
-------

.. py:method:: purge()

    Очищает кеш модуля регулярных выражений

search()
--------

.. py:method:: search(pattern, string, flags=0)

    Проверяет соотвествие с любой частью строки, если соответсвие найдено,
    возвращается :py:class:`Match` иначе None

    .. code-block:: py

        re.search('\d+', '123ilnurgi123')
        # <re.Match object; span=(0, 3), match='123'>


split()
-------

.. py:method:: split(pattern, string, maxsplit=0, flags=0)

    Возвращает список, полученный путем разбиения строки по шаблону

    .. code-block:: py

        re.split(r'\W+', 'Words, words, words.')
        # ['Words', 'words', 'words', '']

        re.split(r'(\W+)', 'Words, words, words.')
        # ['Words', ', ', 'words', ', ', 'words', '.', '']

        re.split(r'\W+', 'Words, words, words.', 1)
        # ['Words', 'words, words.']

        re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
        # ['0', '3', '9']

        re.split(r'(\W+)', '...words, words...')
        # ['', '...', 'words', ', ', 'words', '...', '']

        re.split(r'\b', 'Words, words, words.')
        # ['', 'Words', ', ', 'words', ', ', 'words', '.']

        re.split(r'\W*', '...words...')
        # ['', '', 'w', 'o', 'r', 'd', 's', '', '']

        re.split(r'(\W*)', '...words...')
        # ['', '...', '', '', 'w', '', 'o', '', 'r', '', 'd', '', 's', '...', '', '', '']


sub()
-----

.. py:method:: sub(pattern, repl, string, count=0, flags=O)

    Ищет все совпадения с шаблоном и заменяет их указанным значением.

    Внутри нового фрагмента можно использовать обратные ссылки \номер,
    \g<номер> и \g<название>, соответствующие группам внутри шаблона.

    **repl** может быть и ссылкой на функцию, в котороую будет передаваться объект :py:class:`Match`,
    соответствующий найденному фрагменту.
    Результат, возвра­щаемый этой функцией, служит фрагментом для замены.


subn()
------

.. py:method:: subn(pattern, repl, string, count=0, flags=O)

    Аналогичен :py:meth:`sub`,
    но возвращает кортеж из двух элементов, измененной строки и колчества замен


Match()
-------

.. py:class:: Match()

    .. code-block:: py

        р = re.compile(r"(?P<num>[0-9]+) (?P<str>[a-z]+)")
        p.groups, p.groupindex
        # (2, { 1 num 1 : 1, 1 Str 1 : 2}

        m = p.search("123456string 67890text")
        # < sre.SRE Match object at Ox00FC9DEB>


    .. py:atribute:: endpos

        конечная позиция поиска

        .. code-block:: py

            m.endpos
            # 22


    .. py:atribute:: lastindex

        номер последней группы или None

        .. code-block:: py

            m.lastindex
            # 2


    .. py:atribute:: lastgroup

        название последней группы или None

        .. code-block:: py

            m.lastgroup
            # 'str'


    .. py:atribute:: pos

        начальная позиция поиска

        .. code-block:: py

            m.pos
            # 0


    .. py:attribute:: re

        ссылка на скомпилированный шаблон :py:class:`SRE_Pattern`

        .. code-block:: py

            m.re.groups, m.re.groupindex
            # 2, {'num': 1, 'str': 2}


    .. py:attribute:: string

        искомая строка

        .. code-block:: py

            m.string
            # '123456string 67890text'


    .. py:method:: expand(template)

        Производит замену в строке.

        Внутри указанного шаблона можно использовать обратные ссылки: \номер, \g<номер> и \g<название>

        .. code-block:: py

            р = re.compile(r"<(?P<tag1>[a-z]+)><(?P<tag2>[a-z]+)>")
            m = p.search("<br><hr>")
            m.expand(r"<\2><\1>")
            # '<hr><br>' # \номер

            m.expand(r"<\g<2>><\g<1>>") # \g<номер>
            # '<hr><br>'

            m.expand(r"<\g<tag2>><\g<tag1>>") # \g<название>
            # '<hr><br>'


    .. py:method:: group(args)

        :param args: id или name

        возвращает фрагменты, соответствующие шаблонам

        .. code-block:: py

            m.group(), m.group(O) # полное соответствие шаблону
            # '123456string', '123456string'

            m.group(1), m.group(2) # Обращение по индексу
            # '123456', 'string'

            m.group("num"), m.group("str") # Обращение по названию
            # '123456', 'string'

            m.group(1, 2), m.group("num", "str") # Несколько nараметров
            # ('123456', 'string'), ('123456', 'string')


    .. py:method:: groupdict(default=None)

        :param default: значение для не найденных групп

        Возвращает словарь содержащий значения именованных групп

        .. code-block:: py

            m.groupdict()
            # {'num': '123456', 'str': 'string'}


    .. py:method:: groups(default=None)

        Возвращает кортеж, содержащий значения всех групп или значение по умолчанию.

        .. code-block:: py

            m.groups()
            # '123456', 'strin'

            re.match(r"(\d+)\.(\d+)", "24.1632").groups()
            # ('24', '1632')

            re.match(r"(\d+)\.?(\d+)?", "24").groups()
            # ('24', None)


    .. py:method:: start([group])

        Возвращает индекс начала фрагмента.

        Если параметр не указан, то фрагментом является полное соответствие с шаблоном, в против­ном случае - соответствие с указанной группой.

        Если соответствия нет, то возвращает­ся значение -1

        .. code-block:: py

            р = re.compile(r"(?P<num>[0-9]+)(?P<str>[a-z]+)")
            s = "str123456str"
            m = p.search(s)
            m.start(), m.start(1), m.start('num'), m.start(2), m.start('str')
            # 3, 3, 3, 9, 9


    .. py:method:: end([group])

        Возвращает индекс конца фрагмента.

        Если па­раметр не указан, то фрагментом является полное соответствие с шаблоном, в против­ном случае - соответствие с указанной группой.

        Если соответствия нет, то возвращает­ся значение -1

        .. code-block:: py

            р = re.compile (r"(?P<num>[0-9]+)(?P<str>[a-z]+)")
            s = "str123456str"
            m = p.search(s)
            m.end(), m.end(1), m.end('num'), m.end(2), m.end('str')
            # 12, 9, 9, 12, 12


    .. py:method:: span([group])

        Возвращает кортеж, содержащий начальный и конечный индексы фрагмента.

        Если параметр не указан, то фрагментом является полное соответствие с шаблоном, в противном случае - соответствие с указанной группой.

        Если соответствия нет, то возвращается значение (-1, -1)

        .. code-block:: py

            р = re.compile (r"(?P<num>[0-9]+)(?P<str>[a-z]+)")
            s = "str123456str"
            m = p.search(s)
            m.span()
            # (3, 12)

            m.span(1), m.span("num"), m.span(2), m.span("str")
            # (3, 9), (3, 9), (9, 12), (9, 12)

            s[m.start(1):m.end(1)], s[m.start(2):m.end(2)]
            # '123456', 'str'


SRE_Pattern()
-------------

.. py:class:: SRE_Pattern

    объект возвращаемый методом :py:meth:`compile`


    .. py:attribute:: flags

    .. py:attribute:: groups

        Количесвто груп в шаблоне


    .. py:attribute:: groupindex

        Словарь с названиями групп и их номерами

    .. py:attribute:: pattern


    .. py:method:: findall(string[, pos[, endpos]])

        Аналог :py:meth:`re.findall()`.

        Возвращает список найденных фрагментов.

        Если внутри шаблона есть более одной груnnы, то каждый элемент сnиска будет кортежем, а не строкой.

        .. code-block:: py

            re.compile(r"[0-9]+").findall("2007, 2008, 2009, 2010, 2011")
            # ['2007', '2008', '2009', '2010', '2011']


    .. py:method:: finditer(string[, pos[, endpos]])

        Аналог :py:meth:`re.finditer()`.

        Возвращает итератор найденных фрагментов.

        Если внутри шаблона есть более одной груnnы, то каждый элемент сnиска будет кортежем, а не строкой.


    .. py:method:: fullmatch(string [, start] [, end])

        :param str string: искомая строка
        :parma int start: начальная позиция
        :param int end: конечная позиция

        .. versionadded:: 3.4

        .. code-block:: py

            pattern = re.compile("o[gh]")

            pattern.fullmatch("dog")
            # None

            pattern.fullmatch("ogre")
            # None

            pattern.fullmatch("doggie", 1, 3)
            # <re.Match object; span=(1, 3), match='og'>

    .. py:method:: match(string [, start] [, end])

        :param str string: искомая строка
        :parma int start: начальная позиция
        :param int end: конечная позиция

        Проверяет соотвествие с началом строки, если соответсвие найдено, возвращается :py:class:`Match` иначе None.

        .. code-block:: py

            pattern = re.compile("o")

            pattern.match("dog")
            # None

            pattern.match("dog", 1)
            # <re.Match object; span=(1, 2), match='o'>


    .. py:method:: search(string [, start] [, end])

        :param str string: искомая строка
        :parma int start: начальная позиция
        :param int end: конечная позиция

        Проверяет соотвествие с любой частью строки, если соответсвие найдено, возвращается :py:class:`Match` иначе None

        .. code-block:: py

            pattern = re.compile("d")

            pattern.search("dog")
            # <re.Match object; span=(0, 1), match='d'>

            pattern.search("dog", 1)
            # None


    .. py:method:: split(string, maxsplit)

        Аналогичен :py:meth:`re.split()`

        Возвращает список, полученный путем разбиения строки по шаблону.

        .. code-block:: py

            re.compile(r"[\s, .]+").split("word1, word2\nword3\r\nword4.word5")
            # ['word1', 'word2', 'word3', 'word4', 'word5']


    .. py:method:: sub(repl, string, count=0)

        Аналог :py:meth:`re.sub()`.

        Ищет все совпадения с шаблоном и заменяет их указанным значением.

        Внутри нового фрагмента можно использовать обратные ссылки \номер, \g<номер> и \g<название>, соответствующие группам внутри шаблона.

        В качестве первого параметра можно указать ссылку на функцию. В эту функцию будет передаваться объект :py:class:`Match`,
        соответствующий найденному фрагменту.

        Результат, возвра­щаемый этой функцией, служит фрагментом для замены.

        .. code-block:: py

            р = re.compile(r"<(?P<tag1>[a-z]+)><(?P<tag2>[a-z]+)>")

            p.sub(r"<\2><\1>", "<br><hr>") # \номер
            # <hr><br>'

            р.sub(r"<\g<2>><\g<1>>", "<br><hr>") # \g<номер>
            # '<hr><br>'

            p.sub(r"<\g<tag2>><\g<tag1>>", "<br><hr>") # \g<название>
            # '<hr><br>'


    .. py:method:: subn(repl, string, count=0)

        Аналог :py:meth:`re.subт()`.

        Возвращает кортеж из двух элементов, измененной строки и колчества замен.
