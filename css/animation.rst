Анимации, преобразования и переходы
===================================

Стили, изменение которых приведет к изменению расположения других элементов:

* border
* border-width
* bottom
* display
* clear
* float
* font-family
* font-size
* font-weight
* height
* left
* line-height
* margin
* min-height
* overflow
* overflow-y
* padding
* position
* right
* text-align
* top
* vertical-align
* white-space
* width

Стили, изменение которых приведет к перерисовке других элементов:

* background
* background-image
* background-position
* background-repeat
* background-size
* border-radius
* border-style
* box-shadow
* color
* outline
* outline-color
* outline-style
* outline-width
* text-decoration
* visibility


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

Назначает анимацию, созданной с помощью :ref:`keyframes`

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


transform
---------

Трансформация элемента: масштабирование, вращение, наклон или пермещение.

* perspective

* rotate(<angle>)
* rotateX
* rotateY
* rotate3d

* scale(<number>)
* scaleX
* scaleY
* scaleZ
* scale3d

* skew
* skewX
* skewY

* translate(<horizontal-position>, [<vertical-position>])
* translateX
* translateY
* translateZ
* translate3d

.. code-block:: css

    elem1 {
        transform: rotate(45deg);

        // переместить элемент на 50 пикселей влево
        transform: translate(50px);

        // переместить элемент на 2rem вправо и на 100% вниз
        transform: translate(-2rem, 100%);

        transform: scale(1.5);

        transform: skew(45deg 0) rotate(200deg) translate(100px, 0) scale(.5);
    }


transform-origin
----------------

Точка, в которой применяется трансформация.

.. code-block:: css

    elem1 {
        // transform-origin: <horizontal-position> <vertical-position>;

        transform-origin: left top;

        transform-origin: 0% 100%;

        transform-origin: 10px -100px;
    }


transition
----------

Анимирует изменения CSS свойств элемента

.. code-block:: css

    elem {
        transition:
            transition-property
            transition-duration
            transition-timing-function
            transition-delay;
    }

.. code-block:: css

    elem {
        transition: background-color 1.5s ease-in-out 500ms;
    }


transition-delay
----------------

Время задержки перед началом анимации перехода

.. code-block:: css

    elem1 {
        transition-delay: 2s;
    }

    elem2 {
        transition-delay: 1000ms;
    }


transition-duration
-------------------

Продолжительность анимации перехода

.. code-block:: css

    elem {
        transition-duration: 2s;
    }

    elem1 {
        transition-duration: 2000ms;
    }


transition-property
-------------------

Определяет конкретные css-свойства

.. code-block:: css

    elem {
        transition-property: width, left;
    }

    elem1 {
        transition-property: all;
    }


transition-timing-function
--------------------------

Скорость анимации перехода

* linear
* ease
* easi-in
* easi-out
* easi-in-out

.. code-block:: css

    elem1 {
        transition-timing-function: ease-in-out;
    }

    elem2 {
        transition-timing-function: cubic-bezier(.20, .96, .74, .07);
    }


Слайдшоу на css
---------------

.. code-block:: css

    #slider {
        width: 100%;
        height: 100vh;
        background-position: center center;
        background-size: cover;
        background-repeat: no-repeat;
        backface-visibility: hidden;
        animation: slide 8s linear infinity 0s;
        animation-timing-function: easy-in-out;
        background-image: url('../img/1.jpg');
    }

    @keyframes slide{
        0% {
            background-image: url('../img/1.jpg');
        }
        50% {
            background-image: url('../img/2.jpg');
        }
    }