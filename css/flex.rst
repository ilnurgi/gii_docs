.. title:: css flex

.. meta::
    :description:
        Описание css стиля flex.
    :keywords:
        css flex

flex
====

.. code-block:: html

    <div class="flex-container">
        <div class="flex-item">1</div>
        <div class="flex-item">2</div>
        <div class="flex-item">3</div>
    </div>


.. code-block:: css

    .flex-container {
        /* флекс контейнер, а его потомки - флекс-элементы */
        display: flex;
        background-color: #aff1b6;
    }

    .flex-item {
        /* flex: flex-grow flex-shrink flex-basis; */
        flex: 0 1 auto;
        background-color: #ffcca5;
        padding: 10px;
        margin: 5px;
    }

    .flex-item::nth-child(3) {
        /* толкаем 3 элемент вправо */
        margin-left: auto;

        /* центрируем элемент */
        margin: auto;
    }

.. raw:: html

    <div style="display: flex;background-color: #aff1b6;">
        <div style="flex: 0 1 auto;background-color: #ffcca5;padding: 10px;margin: 5px;">1</div>
        <div style="flex: 0 1 auto;background-color: #ffcca5;padding: 10px;margin: 5px;">2</div>
        <div style="flex: 0 1 auto;background-color: #ffcca5;padding: 10px;margin: 5px;margin-left: auto;">3</div>
    </div>


align-content
-------------

Распределение основных осей вродителе

* center

* space-between

* stretch

.. code-block:: css

    .some-class {
        align-content: center;
    }


align-items
-----------

Выравнивание дочерних элементов по второстепенной оси

.. code-block:: css

    .flex-container {
        display: flex;
        align-item: stretch;
        background-color: #aff1b6;
        height: 70px;
    }

    .flex-item {
        background-color: #ffcca5;
        padding: 10px;
        margin: 5px;
    }

* **baseline**

.. raw:: html

    <div style="display: flex;background-color: #aff1b6;flex-direction: row;height: 80px;align-items: baseline;">
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;">1</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;">2</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;">3</div>
    </div>

* **flex-start** - выравнивание по верхнему краю

.. raw:: html

    <div style="display: flex;background-color: #aff1b6;flex-direction: row;height: 80px;align-items: flex-start;">
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;">1</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;">2</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;">3</div>
    </div>

* **flex-end** - выравнивание по нижнему краю

.. raw:: html

    <div style="display: flex;background-color: #aff1b6;flex-direction: row;height: 80px;align-items: flex-end;">
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;">1</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;">2</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;">3</div>
    </div>

* **center** - по центру

.. raw:: html

    <div style="display: flex;background-color: #aff1b6;flex-direction: row;height: 80px;align-items: center;">
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;">1</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;">2</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;">3</div>
    </div>

* **stretch** - по максимальному, по умолчанию

.. raw:: html

    <div style="display: flex;background-color: #aff1b6;flex-direction: row;height: 80px;align-items: stretch;">
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;">1</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;">2</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;">3</div>
    </div>


align-self
----------

Выравнивание самого дочернего элемента

* auto - по умолчанию, как в родительском

* baseline

* flex-start - выравнивание по верхнему краю

* flex-end - выравнивание по нижнему краю

* center - по центру

* stretch - по максимальному

.. code-block:: css

    .flex-item {
        align-self: auto;
    }


flex-basis
----------

Задает минимальную ширину дочернего элемента.

Если дочерний элемент находится на основной оси с другими элементами,
то его ширина не будет изменяться при уменьшении ширины родительского элемента,
другие элементы или сам элемент будут переходить на другие оси.

Если дочерний элемент находится на основной оси один,
то его ширина будет уменьшаться при уменьшении ширины родительского элемента.

* auto - по умолчанию

.. code-block:: css

    .flex-item {
        flex-basis: 300px;
    }


flex-direction
--------------

Направление основной оси

.. code-block:: css

    .flex-container {
        display: flex;
        flex-direction: row;
        background-color: #aff1b6;
        height: 70px;
    }

    .flex-item {
        background-color: #ffcca5;
        padding: 10px;
        width: 30px;
        height: 30px;
        margin: 5px;
    }

* **column** - сверху вних

.. raw:: html

    <div style="display: flex;background-color: #aff1b6;flex-direction: column;height: 200px;">
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;width: 30px;">1</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;width: 30px;">2</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;width: 30px;">3</div>
    </div>

* **column-reverse** - снизу вверх

.. raw:: html

    <div style="display: flex;background-color: #aff1b6;flex-direction: column-reverse;height: 200px;">
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;width: 30px;">1</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;width: 30px;">2</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;width: 30px;">3</div>
    </div>

* **row** - по умолчанию, слева направо

.. raw:: html

    <div style="display: flex;background-color: #aff1b6;flex-direction: row;height: 70px;">
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;width: 30px;">1</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;width: 30px;">2</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;width: 30px;">3</div>
    </div>

* **row-reverse** - справа налево

.. raw:: html

    <div style="display: flex;background-color: #aff1b6;flex-direction: row-reverse;height: 70px;">
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;width: 30px;">1</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;width: 30px;">2</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;width: 30px;">3</div>
    </div>


flex-flow
---------

.. code-block:: css

    .flex-container {
        display: flex;
        flex-flow: column;
        background-color: #aff1b6;
        height: 70px;

    }

    .flex-item {
        background-color: #ffcca5;
        padding: 10px;
        width: 30px;
        height: 30px;
        margin: 5px;
    }

* **column**

.. raw:: html

    <div style="display: flex;background-color: #aff1b6;flex-flow: column;height: 200px;">
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;width: 30px;">1</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;width: 30px;">2</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;width: 30px;">3</div>
    </div>


flex-grow
---------

Степень жадности элемента

Если значение отличное от 0,
то по ширине элемент займет все пустое пространство по главной оси.

* 0 - по умолчанию, элемент не жадный

.. code-block:: css

    .flex-item {
        flex-grow: 0;
    }

.. raw:: html

    <div style="display: flex;background-color: #aff1b6;flex-direction: row;height: 80px;">
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;flex-grow: 1;">1</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;flex-grow: 2;">2</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;flex-grow: 1;">1</div>
    </div>

flex-shrink
-----------

Степень/скорость сжимаемости элемента

* 0 - элемент не сжимаемый

* 1 - по умолчанию, элемент сжимаемый

.. code-block:: css

    .flex-item {
        flex-shrink: 1;
    }


flex-wrap
---------

Перенос элементов в элементе

* no-wrap - по умолчанию, не переносить

* wrap - переносить

* wrap-reverse

.. code-block:: css

    .flex-container {
        flex-wrap: wrap;
    }


justify-content
---------------

Заполнение оси

.. code-block:: css

    .flex-container {
        flex-direction: row;
        background-color: #aff1b6;
        height: 70px;
        justify-content: flex-end;
    }

    .flex-item {
        background-color: #ffcca5;
        padding: 10px;
        width: 30px;
        height: 30px;
        margin: 5px;
    }

* **flex-end** - относительно конца

.. raw:: html

    <div style="display: flex;background-color: #aff1b6;flex-direction: row;height: 70px;justify-content: flex-end;">
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;width: 30px;">1</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;width: 30px;">2</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;width: 30px;">3</div>
    </div>

* **flex-start** - относительно начала

.. raw:: html

    <div style="display: flex;background-color: #aff1b6;flex-direction: row;height: 70px;justify-content: flex-start;">
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;width: 30px;">1</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;width: 30px;">2</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;width: 30px;">3</div>
    </div>

* **center** - от центра

.. raw:: html

    <div style="display: flex;background-color: #aff1b6;flex-direction: row;height: 70px;justify-content: center;">
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;width: 30px;">1</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;width: 30px;">2</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;width: 30px;">3</div>
    </div>

* **space-around** - растягивает по оси, оставляя равные промежутки между элементами

.. raw:: html

    <div style="display: flex;background-color: #aff1b6;flex-direction: row;height: 70px;justify-content: space-around;">
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;width: 30px;">1</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;width: 30px;">2</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;width: 30px;">3</div>
    </div>

* **space-between** - растягивает по оси, оставляя равные промежутки между элементами

.. raw:: html

    <div style="display: flex;background-color: #aff1b6;flex-direction: row;height: 70px;justify-content: space-between;">
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;width: 30px;">1</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;width: 30px;">2</div>
        <div style="background-color: #ffcca5;padding: 10px;margin: 5px;height: 30px;width: 30px;">3</div>
    </div>


order
-----

Задает порядковый номер элементу по флекс контейнере

.. code-block:: html

    .flex-item {
        order: -1;
    }
