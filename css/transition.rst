.. title:: css transition

.. meta::
    :description:
        Описание css стиля transition.
    :keywords:
        css transition

transition
==========

Анимирует изменения CSS свойств элемента

.. code-block:: text

    div {
        transition:
            transition-property
            transition-duration
            transition-timing-function
            transition-delay;
    }

.. code-block:: css

    div {
        transition: background-color 1.5s ease-in-out 500ms;
        transition: all 1.5s ease-in-out 500ms;
    }


transition-delay
----------------

Время задержки перед началом анимации перехода

.. code-block:: css

    div {
        transition-delay: 2s;
        transition-delay: 1000ms;
    }


transition-duration
-------------------

Продолжительность анимации перехода

.. code-block:: css

    div {
        transition-duration: 2s;
        transition-duration: 2000ms;
    }


transition-property
-------------------

Определяет конкретные css-свойства

.. code-block:: css

    div {
        transition-property: width, left;
        transition-property: all;
        transition-property: transform;
    }


transition-timing-function
--------------------------

Скорость анимации перехода

* **ease**
* **easi-in**
* **easi-out**
* **easi-in-out**
* **linear**
* **steps**

.. code-block:: css

    div {
        transition-timing-function: ease-in-out;
        transition-timing-function: cubic-bezier(.20, .96, .74, .07);
        transition-timing-function: steps(6, end);
    }
