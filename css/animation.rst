Анимации, преобразования и переходы
===================================



animation
---------

Анимация

.. code-block:: css

    elem {
        animation:
            animation-name
            animation-duration
            animation-timing-function
            animation-delay
            animation-iteration-count
            animation-direction
            animation-fill-mode
            animation-play-state;
    }

.. code-block:: css

    div {
        animation: fadeOut 2s ease-in-out 2 alternate 5s forwards, glow 5s;
    }


animation-delay
---------------

Время задержки начала анимации

.. code-block:: css

    elem1 {
        animation-delay: 2s;
    }

    elem2 {
        animation-delay: 1000ms;
    }


animation-direction
-------------------

Стартовая точка анимации, для последующей анимации

* alternate
* alternate-reverse
* normal - по умолчанию
* reverse

.. code-block:: css

    elem {
        animation-direction: alternate;
    }


animation-duration
------------------

Продолжительность анимации

.. code-block:: css

    elem1 {
        animation-duration: 2s;
    }

    elem2 {
        animation-duration: 1000ms;
    }


animation-fill-mode
-------------------

Стилизация элемента вначале и-или в конце

* backwards

* forwards

* both

.. code-block:: css

    elem {
        animation-fill-mode: backwards;
    }


animation-iteration-count
-------------------------

Количество запусков анимации

.. code-block:: css

    elem1 {
        animation-iteration-count: 2;
    }

    elem2 {
        animation-iteration-count: infinite;
    }


animation-name
--------------

Назначает анимацию, созданной с помощью `keyframes`

.. code-block:: css

    elem {
        animation-name: myAnimation;
    }


animation-play-state
--------------------

Управляет проигрыванием анимации, например можно использовать с псевдоклассом `hover`

* pause

* running

.. code-block:: css

    elem {
        animation-play-state: pause
    }


animation-timing-function
-------------------------

Скорость анимации в течении выделенной ей периода.

* ease
* easi-in
* easi-out
* easi-in-out
* cubic-bezier(x1, y1, x2, y2)
* linear
* steps(number, direction <optional>)
    * direction - start or end

.. code-block:: css

    elem1 {
        animation-timing-function: ease-in-out;
    }

    elem2 {
        animation-timing-function: cubic-bezier(.20, .96, .74, .07);
    }


keyframes
---------

Созданет анимацию с указанным имененм,
которую потом можно будет применить к любому элементу страницы.

.. code-block:: css

    @keyframes myAnimation {
        from {
            background-color: black;
        }
        to {
            background-color: whote;
        }
    }

.. code-block:: css

    // плавно опускает элемент
    @keyframes bounce {
        0% {
            transform: translateY(-2000px);
        }
        70% {
            transform: translateY(30px);
        }
        90% {
            transform: translateY(-10px);
        }
        100% {
            transform: translateY(0);
        }
    }
    .some-class {
        animation: bounce 0.6s;
    }

.. code-block:: css

    // встряска формы
    @keyframes shake {
        0%, 100% {
            transform: translateX(0);
        }
        10%, 30%, 50%, 70%, 90% {
            transform: translateX(-10px);
        }
        20%, 40%, 60%, 80% {
            transform: translateX(10px);
        }
    }
    .some-class {
        animation: shake 0.6s;
    }





