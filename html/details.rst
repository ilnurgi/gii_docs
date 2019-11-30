.. title:: html details

.. meta::
    :description:
        Описание html элемента details
    :keywords:
        html details

details
=======

Аккордеон. Область, которая может разворачиваться и сворачиваться.

.. code-block:: html

    <details open>
        <summary>Дополнительная информация</summary>
        <p>Текст</p>
    </details>

.. raw:: html

    <details open>
        <summary>Дополнительная информация</summary>
        <p>Текст</p>
    </details>


.. code-block:: css

    /* Убираем стандартный маркер Chrome */
    details summary::-webkit-details-marker {
        display: none
    }

    /* Убираем стандартный маркер Firefox */
    details > summary {
        list-style: none;
    }

    /* Добавляем собственный маркер для закрытого состояния */
    details summary:before {
        content: '+';
    }

    /* Добавляем собственный маркер для открытого состояния */
    details[open] summary:before {
        content: '-';
    }

.. raw:: html

    <style>
        details .my-summary::-webkit-details-marker {
            display: none
        }
        details > .my-summary {
            list-style: none;
        }

        details .my-summary:before {
            content: '+';
            margin-right: 7px;
        }

        /* Добавляем собственный маркер для открытого состояния */
        details[open] .my-summary:before {
            content: '-';
        }
    </style>
    <details open>
        <summary class="my-summary">Дополнительная информация</summary>
        <p>Текст</p>
    </details>
