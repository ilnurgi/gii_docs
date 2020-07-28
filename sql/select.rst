.. title:: sql select

.. meta::
    :description: 
        Справочная информация по sql, оператор select.
    :keywords: 
        sql select

SELECT
======

Оператор выборки данных из БД

.. code-block:: text
    
    SELECT [ALL | DISTINCT]
        [<название таблицы>.]<поле>,
        ...
        [FROM <таблица> [AS <псевдоним>][,] ]
        [WHERE <условие>]
        [[GROUP BY <название поля>] [HAVING <условие>]]
        [ORDER BY <название поля> [COLLATE BINARY | NOCASE] [ASC | DESC][, ...]]
        [LIMIT <ограничение>]

.. code-block:: sql

    SELECT * FROM table;

.. code-block:: sql

    SELECT 
      table1.name
      , table2.name 
    FROM 
      table1, table2 
    WHERE 
      table1.num = table2.num

.. code-block:: sql

    SELECT
      *
    FROM (
      VALUES
        (1, 'ilnurgi1')
        , (2, 'ilnurgi2')
    ) t(p_id, p_name)

    /*
    p_id | p_name
    -----+-------
    1    | ilnurgi1
    2    | ilnurgi2
    */



ALL, DISTINCT
-------------

ALL - в результат попадут все значения, DISTINCT - в результат попадут уникальные значения

.. code-block:: sql

    SELECT distinct 
      table1.name
    FROM 
      table1, table2 
    WHERE 
      table1.num = table2.num


FROM
----

Откуда достать данные, таблица, подзапрос, CTE

.. code-block:: sql

    SELECT distinct 
      table1.name
    FROM 
      table1, table2 
    WHERE 
      table1.num = table2.num


INNER JOIN
----------

Соединение двух таблиц, в выборку попадут только те записи из обоих таблиц, 
которые удовлетворяют условию соединения.

.. code-block:: sql

    SELECT 
      table1.name
      , table2.name
    FROM 
      table1

      INNER JOIN
        table2 
         ON
            table1.name = table2.name


LEFT JOIN
---------

Соединение двух таблиц, в выборку попадут все записи из основной таблицы, 
из присоединямой таблицы попадут только те записи которые удовлетворяют условию соединения.

.. code-block:: sql

    SELECT 
      table1.name
      , table2.name
    FROM 
      table1

      LEFT JOIN
        table2 
         ON
            table1.name = table2.name


RIGHT JOIN
----------

Соединение двух таблиц, в выборку попадут все записи из присоединяемой таблицы, 
из основной таблицы попадут только те записи которые удовлетворяют условию соединения.

.. code-block:: sql

    SELECT 
      table1.name
      , table2.name
    FROM 
      table1

      RIGHT JOIN
        table2 
         ON
            table1.name = table2.name


OUTER JOIN
----------

Соединение двух таблиц, в выборку попадут все записи из таблиц.

.. code-block:: sql

    SELECT 
      table1.name
      , table2.name
    FROM 
      table1

      OUTER JOIN
        table2 
         ON
            table1.name = table2.name


WHERE
-----

Оператор условия, накладывает фильтр на данные

.. code-block:: sql

    SELECT distinct 
      table1.name
    FROM 
      table1, table2 
    WHERE 
      table1.num = table2.num


GROUP BY
--------

Позволяет сгруппировать несколько записей, полезна при использовании `function_aggregate`


HAVING
------

Фильтрует уже сгруппированные данные по условию

.. code-block:: sql

    select
      user_id
      , avg(rating) avg_rating
    from
      ratings
    group by
      user_id
    having 
      avg(rating) < 4.5
      -- в случае с перименовыванием поля, можно обратиться к алиасу поля
      -- avg_rating < 4.5


ORDER BY
--------

Cортировка выбранных значений

* **ASC** - по возрастанию
* **DESC** - по убыванию

.. code-block:: sql

  select
    *
  from
    table
  order by
    id asc


LIMIT
-----

ограничивает количество записей в выборке

    * `LIMIT <количесвто записей>`
    * `LIMIT <начальная позиция>, <количесвто записей>`
    * `LIMIT <количесвто записей> OFFSET <начальная позиция>`

.. code-block:: sql

    SELECT 10=10, 5=10;
    # 1 | 0


CASE
----

условное выражение

.. code-block:: text

    CASE выражение 
        WHEN выражение
        THEN выражение
        ELSE выражение
    END

.. code-block:: sql

    SELECT 
      CASE sname 
        WHEN 'Peel' 
          THEN 'Peal' 
      END
    FROM table;

    SELECT 
      CASE sname 
        WHEN 'Peel' 
          THEN 'Peal' 
        ELSE sname 
      END
    FROM table;

    -- использование предиката
    SELECT 
      CASE 
        WHEN sname 'Peel' 
          THEN 'Peal' 
        ELSE sname 
      END
    FROM table;


CAST
----

оператор преобразования одного типа в другой

.. code-block:: sql

    SELECT CAST(onum AS CHAR) FROM table

COALESCE
--------

принимает значения, выводится первое не NULL

.. code-block:: text

    COALESCE (выражение, ....)

.. code-block:: sql

    SELECT 
      COALESCE(snum, cnum) num
      , COALESCE("null_row", 0) amount
    FROM table
    -- 5, 0


DISTINCT
--------
    
Оператор указывает, выбрать только уникальные записи

.. code-block:: text

    SELECT DISTINCT 
        <столбцы> 
    FROM <таблица>;

ESCAPE
------

Оператор устанавливает символ, которые будет экранировать символы

.. code-block:: text

    SELECT 
      <столбцы> 
    FROM 
      <таблица> 
    WHERE 
      <условие> 
    ESCAPE 
      <escape>;

.. code-block:: sql
    
    SELECT 
      * 
    FROM 
      table 
    WHERE 
      name LIKE 'G\_00_' 
    -- вернет G_002, _ - экранируется
    ESCAPE 
      '\';


EXCEPT (MINUS)
--------------

Объединяет запросы по разности

.. code-block:: sql

    SELECT 
        * 
    FROM table1 
    EXCEPT 
        SELECT 
            * 
        FROM table2

EXISTS
------

принимает подзапрос в качетсве аргумента, и выдает TRUE при наличии в подзапросе выходных данных, иначе FALSE

.. code-block:: sql

    SELECT 
        * 
    FROM table1 
    WHERE EXISTS (
        SELECT 
            * 
        FROM table1
        WHERE id = 1)

FULL OUTER JOIN 
---------------

полное внешнее соединение, записи левой и правой таблицы, в которых не было найдено совпадений, столбцы из правой и левой таблицы заполняются NULL.

.. code-block:: sql

    SELECT 
        * 
    FROM table1 
    FULL OUTER JOIN table2
    ON table1.table2_id = table2.id

GROUP BY
--------

группировка результата по колонкам

HAVING
------

сортировка результата по какому то условию

INNER JOIN
----------

внутреннее соединение, несовпадающие строки обеих таблиц исключаются

.. code-block:: sql

    SELECT table2.title, table1.description 
        FROM table1
    INNER JOIN table1
        ON table2.table1_id = table1.table1_id

INTERSECT
---------

Объединяет запросы по общему значению, т.е. находит пересечение строк запросов

.. code-block:: sql

    SELECT 
        * 
    FROM table1 
    INTERSECT 
        SELECT 
            * 
        FROM table2

LEFT OUTER JOIN
---------------

левое внешнее соединение, записи левой таблицы, в которых не было найдено совпадений, столбцы из правой таблицы заполняются NULL.

.. code-block:: sql

    SELECT 
      * 
    FROM 
      table1 
      
      LEFT OUTER JOIN table 2 
        ON 
          table1.table2_id = table2.id

NULLIF
------

принимает два аргумента, если совпдают будет NULL, иначе одно из двух значений

.. code-block:: sql

    SELECT 
      NULLIF(snum, 1001)
    FROM 
      table


ORDER BY
--------

Оператор упорядочивания

.. code-block:: text

    SELECT 
      <столбцы> 
    FROM 
      <таблица> 
    ORDER BY 
      <столбцы> ASC|DESC;

    ASC - сортировка по убыванию
    DESC - сортировка по возрастанию

.. code-block:: sql

    SELECT 
      * 
    FROM 
      table 
    WHERE 
      id in (1, 2, 3); 

    SELECT 
      * 
    FROM 
      table 
    WHERE 
      id BETWEEN 1 AND 3; 

    SELECT 
      * 
    FROM 
      table 
    WHERE 
      --name заканчивается на G
      name LIKE 'G%'; 

    SELECT 
      * 
    FROM 
      table 
    WHERE 
      -- вернет bat, bit ..., '_' - любой 1 символ
      name LIKE 'b_t'; 


RIGHT OUTER JOIN
----------------

правое внешнее соединение, записи правой таблицы, в которых не было найдено совпадений, столбцы из левой таблицы заполняются NULL.

.. code-block:: sql
    
    SELECT 
        * 
    FROM table1
    RIGHT OUTER JOIN table2
        ON table1.table2_id = table2.id

UNION
-----

оператор объединения запросов, выводит данные запроса последовательно, исключая дублирующиеся записи

.. code-block:: sql

    SELECT 
        * 
    FROM table1 
    UNION 
        SELECT 
            * 
        FROM table2

UNION JOIN
-----------

Результатом соединение двух таблиц А и Б будут строки со всеми столбцами из таблицы А, дополненные столбцами из таблицы Б с NULL значениями. Затем будут выведены аналогично из таблицы Б.

.. code-block:: sql

    SELECT 
        * 
    FROM table1 
    UNION 
        SELECT 
            * 
        FROM table2

WHERE
-----

Предикат, оператор условия, отбирает записи по каким либо условиям

=, >, <, >=, <=, <>, and, or, not, NULL

.. code-block:: text

    SELECT 
      <столбцы> 
    FROM 
      <таблица> 
    WHERE 
      <условие>;

.. code-block:: sql

    SELECT 
      table1.name as name1
      , table2.name as name2
    FROM 
      table1, table2 
    WHERE 
     table1.name = table.name;
    
    -- подзапрос
    SELECT 
      * 
    FROM 
      table1 
    WHERE 
      id = (
        SELECT 
          id 
        FROM 
          table2
      );


Дата функции
------------

=============== ====
=============== ====
DAY()           Извлекает день месяца из даты. 
MONTH(МЕСЯЦ)
YEAR(ГОД)
HOUR(ЧАСЫ)
SECOND(СЕКУНДЫ)
WEEKDAY()       Извлекает день недели из даты.
=============== ====

Мат функции
-----------

============ ====
============ ====
ABX(x)
CEIL(x)
FLOOR(x)
GRATEST(x,y) большее
LEAST(x,y)   меньшее
MOD(x, y)    остаток от определения
POWER(x, y)  степень
ROUND(x,y)
SING(X)      Возвращает минус если X < 0, или плюс если X > 0.
SQRT (X)     Возвращает квадратный корень из X.
============ ====

Cимвольные функции
------------------

============ ====
============ ====
LEFT(,X)     Возвращает крайние левые(старшие) символы X из строки.
RICHT(,X)    Возвращает символы X младшего разряда из строки
ASCII()      Возвращает код ASCII которым представляется строка в памяти компьютера.
CHR()        Возвращает принтерные символы кода ASCII.
VALUE()      Возвращает математическое значение для строки. Считается что строка имеет тип CHAR или VARCHAR, но состоит из чисел.
VALUE('3')   произведет число 3 типа INTEGER.
UPPER()      Преобразует все символы строки в символы верхнего регистра.
LOWER()      Преобразует все символы строки в символы нижнего регистра.
INlTCAP()    Преобразует символы строки в заглавные буквы. В некоторых реализациях может иметь название - PROPER.
LENGTH()     Возвращает число символов в строке.
||           Объединяет две строки в выводе, так чтобы после первой немедленно следовала вторая. (значек || называется оператором сцепления).
LPAD(,X,'*') Дополняет строку слева звездочками '*', или любым другим указанным символом, с колличестве, определяемом X.
RPAD(,X, ")  То же самое что и LPAD, за исключением того, что дополнение делается справа.
SUBSTR(,X,Y) Извлекает Y символ
ISNULL(x, y) x - столбец, y - значение. проверяет столбец на наличие NULL, и если NULL то вернет указанное значение
============ ====

