.. title:: css grid

.. meta::
    :description:
        Описание css стиля grid.
    :keywords:
        css grid

grid
====

grid
----

.. code-block:: text

    .container {
        display: grid;
        grid:
            <grid-template> |
            <grid-template-rows> /
            [auto-flow && dense?]
            <grid-auto-columns>?|
            [auto-flow && dense?]
            <grid-autwo-rows>? /
            <grid-template-columns>;
    }


.. code-block:: css

    .container {
        grid: 100px 300px / 3fr 1fr;
        /*
            детальное описание
            grid-template-rows: 100px 300px;
            grid-template-columns: 3fr 1fr;
        */
    }


.. code-block:: css

    .container {
        display: grid;
        grid-gap: 20px;
        grid:
            "one one" 200px
            "two four"
            "three four"
            / 1fr 2fr;
        /*
            детальное описание
            grid-template-areas: "one one" "two four" "three four";
            grid-template-columns: 1fr 2fr;
            grid-template-rows: 200px;
        */
    }


.. code-block:: css

    .container {
        grid: 100px 300px / auto-flow 200px;
        /*
            детальное описание
            grid-template-rows: 100px 300px;
            grid-auto-flow: column;
            grid-auto-columns: 200px;
        */
    }


.. code-block:: css

    /*
        Задаем количесвто элементов в 1 колонке, в данном случае 4.
        Т.е. после каждого 4 элемента в колонке, будет создаваться новая колонка.
    */
    ul {
        display: grid;
        grid-template-rows: auto auto auto auto;
        grid-template-rows: repeat(4, auto);
        grid-auto-flow: column;
    }


.. code-block:: html

    <style>
        .grid-container {
            height: 100px;
            width: 300px;
            background: gray;
            display: grid;
        }
        .grid-item {
            border: 1px solid black;
        }
    </style>
    <div class="grid-container">
        <div class="grid-item"></div>
        <div class="grid-item"></div>
    </div>

.. raw:: html

    <div style="height:100px;width:300px;background:gray;display:grid;">
        <div style="border:1px solid black;">
        </div>
        <div style="border:1px solid black;">
        </div>
    </div>


grid-area
---------

.. code-block:: text

    .container {
        grid-area: grid-row-start / grid-column-start / grid-row-end / grid-column-end;
    }

.. code-block:: css

    .container {
        grid-area: 2 / 2 / 3 / 3;
    }


grid-auto-flow
--------------

.. code-block:: css

    .container {
        grid-auto-flow: row;  /* default */
        grid-auto-flow: column;  /* default */
    }


grid-auto-rows
--------------

Автоматическое создание строк

.. code-block:: css

    .container {
        grid-auto-rows: 200px;
    }


grid-colum
----------

.. code-block:: text

    .item {
        grid-colum: grid-colum-start / grid-colum-end;
    }

.. code-block:: css

    .item {
        grid-colum: 1 / 4;
        grid-colum: col-1-start / col-end;

        /* от начала до конца */
        grid-colum: 1 / -1;
    }


grid-colum-end
--------------

.. code-block:: css

    .item {
        grid-colum-end: 4;
        grid-colum-end: col-2-end;
    }


grid-column-gap
---------------

Задает отступ между столбцами

.. code-block:: css

    .container {
        grid-column-gap: 20px;
    }


grid-colum-start
----------------

.. code-block:: css

    .item {
        grid-colum-start: 1;
        grid-colum-start: col-1-start;
    }


grid-gap
--------

Отступ между ячейками сетки

.. code-block:: css

    .container {
        grid-gap: 20px;
    }


grid-row
----------

.. code-block:: text

    .item {
        grid-row: grid-row-start / grid-row-end;
    }
.. code-block:: css

    .item {
        grid-row: 1 / 4;
        grid-row: row-1-start / row-end;

        /* от начала до конца */
        grid-row: 1 / -1;
    }


grid-row-gap
------------

Задает отступ между строками

.. code-block:: css

    .container {
        grid-row-gap: 20px;
    }


grid-row-end
------------

.. code-block:: css

    .item {
        grid-row-end: 4;
        grid-row-end: row-2-end;
    }


grid-row-start
----------------

.. code-block:: css

    .item {
        grid-row-start: 1;
        grid-row-start: row-2-start;
    }


grid-template-areas
-------------------

Настройка грида через области

.. code-block:: css

    .container {
        grid-template-areas:
            "header header"
            "sidebar content"
            ". footer";
        /* точка указывает на пустую ячейку */
    }

.. code-block:: html

    <style>
        .grid-container {
            height: 200px;
            width: 300px;
            display: grid;
            grid-template-areas:
                "header header"
                "sidebar content"
                ". footer";
        }
        .header {
            background-color: red;
            grid-area: header;
        }
        .sidebar {
            background-color: yellow;
            grid-area: sidebar;
        }
        .content {
            background-color: blue;
            grid-area: content;
        }
        .footer {
            background-color: green;
            grid-area: footer;
        }
    </style>
    <div class="grid-container">
        <div class="header"></div>
        <div class="sidebar"></div>
        <div class="content"></div>
        <div class="footer"></div>
    </div>

.. raw:: html

    <style>
        .grid-container {
            height: 200px;
            width: 300px;
            display: grid;
            grid-template-areas:
                "header header"
                "sidebar content"
                ". footer";
        }
        .header {
            background-color: red;
            grid-area: header;
        }
        .gr-sidebar {
            background-color: yellow;
            grid-area: sidebar;
        }
        .content {
            background-color: blue;
            grid-area: content;
        }
        .footer {
            background-color: green;
            grid-area: footer;
        }
    </style>
    <div class="grid-container">
        <div class="header"></div>
        <div class="gr-sidebar"></div>
        <div class="content"></div>
        <div class="footer"></div>
    </div>


grid-template-columns
---------------------

Задает ширину колонок

.. code-block:: css

    .container {
        display: grid;

        /* фиксированная ширина колонок */
        grid-template-columns: 100px 100px 100px;

        /* 4 колонки с одинаковой шириной */
        grid-template-columns: repeat(4, 1fr);

        /* 4 колонки с широной по минимальному контенту */
        grid-template-columns: repeat(4, min-content);

        /* 4 колонки с широной по максимальному контенту */
        grid-template-columns: repeat(4, max-content);

        /* 2 колонки с указанием минимальной и максимальной ширины */
        grid-template-columns: minmax(200px, 1fr) minmax(350px, 1fr);

        /* 3 колонки крайние авто ширина, центральная  */
        grid-template-columns: auto fit-content(800px) auto;

        /* 2 колонки левая по минимальному контенту правая по максимальной */
        grid-template-columns: min-content max-content;

        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        grid-template-columns: repeat(3, [col-start] 1 fr [col-end]);

        /* ручное задание для номеров границ столбцов */
        grid-template-column: [col-1-start] 1fr [col-2-start] 1fr [col-2-end];
    }

.. code-block:: html

    <style>
        .grid-container {
            height: 100px;
            width: 300px;
            background: gray;
            display: grid;
            grid-template-columns: 100px 100px;
        }
        .grid-item {
            border: 1px solid black;
        }
    </style>
    <div class="grid-container">
        <div class="grid-item"></div>
        <div class="grid-item"></div>
    </div>

.. raw:: html

    <div style="height:100px;width:300px;background:gray;display:grid;grid-template-columns: 100px 100px;">
        <div style="border:1px solid black;">
        </div>
        <div style="border:1px solid black;">
        </div>
    </div>


grid-template-rows
------------------

Задает высоту для строк

.. code-block:: css

    .container {
        display: grid;
        grid-template-rows: 50px 50px;

        /* ручное задание для номеров границ строк */
        grid-template-rows: [row-1-start] 1fr [row-2-start] 1fr [row-2-end];

        grid-template-columns: repeat(3, [row-start] 1 fr [row-end]);
    }


Выравнивание блоков
-------------------

Для выравнивания используем:

* **align-items**, **justify-items**

    * **auto**
    * **normal**
    * **start**
    * **end**
    * **center**
    * **stretch**
    * **baseline**
    * **first baseline**
    * **last baseline**

* **align-self**, **justify-self**

    * **auto**
    * **normal**
    * **start**
    * **end**
    * **center**
    * **stretch**
    * **baseline**
    * **first baseline**
    * **last baseline**

* **align-content**, **justify-content**

    * **normal**
    * **start**
    * **end**
    * **center**
    * **stretch**
    * **space-around**
    * **space-between**
    * **space-evenly**
    * **baseline**
    * **first baseline**
    * **last baseline**

.. code-block:: css

    .container {
        align-items: center;
        justify-items: center;
    }

    .item {
        justify-self: center:
        align-self: center;
    }
