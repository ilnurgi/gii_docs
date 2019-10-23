.. title:: css grid

.. meta::
    :description: 
        Описание grid стилей css.
    :keywords: 
        css grid

grid
====

grid
----

.. code-block:: text

    display: grid;
    grid: 
        <grid-template> | 
        <grid-template-rows> / 
        [auto-flow && dense?] 
        <grid-auto-columns>?| 
        [auto-flow && dense?] 
        <grid-autwo-rows>? / 
        <grid-template-columns>;

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


grid-autwo-rows
---------------

Автоматическое создание строк 

.. code-block:: css

    .wrapper{
        grid-autwo-rows: 200px;
    }

    
grid-colum
----------

.. code-block:: css

    .item1 {
        grid-colum: 
            grid-colum-start/
            grid-colum-end;

        grid-colum: 1/4;

        /* от начала до конца */
        grid-colum: 1/-1;
    }


grid-colum-end
--------------

.. code-block:: css

    .item1 {
        grid-colum-end: 4;
    }


grid-colum-start
----------------

.. code-block:: css

    .item1 {
        grid-colum-start: 1;
    }


grid-gap
--------

Отступ между ячейками сетки

.. code-block:: css

    .wrapper {
        grid-gap: 20px;
    }


grid-row
----------

.. code-block:: css

    .item1 {
        grid-row: 
            grid-row-start/
            grid-row-end;

        grid-row: 1/4;

        /* от начала до конца */
        grid-row: 1/-1;
    }

    
grid-row-end
--------------

.. code-block:: css

    .item1 {
        grid-row-end: 4;
    }


grid-row-start
----------------

.. code-block:: css

    .item1 {
        grid-row-start: 1;
    }


grid-template-areas
-------------------

Настройка грида через области

.. code-block:: css

    grid-template-areas: 
        "header header"
        "sidebar content"
        ". footer";
    /* точка указывает на пустую ячейку */
    
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

Настройка колонок

.. code-block:: css
    
    .wrappper {
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
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
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

Настройка строк

.. code-block:: css

    .wrappper {
        display: grid;
        grid-template-rows: 50px 50px;
    }


.. code-block:: css

    .grid {
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

    .item1 {
        grid-area: one;
    }

    .item2 {
        grid-area: two;
    }

    .item3 {
        grid-area: three;
    }

    .item4 {
        grid-area: four;
    }


.. code-block:: css

    .grid {        
        grid: 100px 300px / 3fr 1fr;
        /*
            детальное описание
            grid-template-rows: 100px 300px;
            grid-template-columns: 3fr 1fr;            
        */
    }


.. code-block:: css

    .grid {
        grid: auto-flow / 200px 1fr;
        /*
            детальное описание
            grid-auto-flow: row;
            grid-template-columns: 200px 1fr;
        */
    }


.. code-block:: css

    .grid {
        grid: 100px 300px / auto-flow;
        /*
            детальное описание
            grid-template-rows: 100px 300px;
            grid-auto-flow: column;
        */
    }


.. code-block:: css

    .grid {
        grid: 100px 300px / auto-flow 200px;
        /*
            детальное описание
            grid-template-rows: 100px 300px;
            grid-auto-flow: column;
            grid-auto-columns: 200px;
        */
    }


Задаем количесвто элементов в 1 колонке, в данном случае 4. 
Т.е. после каждого 4 элемента в колонке, будет создаваться новая колонка.

.. code-block:: css
    
    ul {
        display: grid;
        
        grid-template-rows: auto auto auto auto;        
        grid-template-rows: repeat(4, auto);
        grid-auto-flow: column;
    }