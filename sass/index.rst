Sass
====

.. code-block:: sh

    # установка
    npm install sass

    # версия
    sass --version
    # 1.6.2

    # компиляция
    sass main.sass style.css
    sass main.scss style.css

Блоки
-----

Выделяются отсупами

.. code-block:: scss

    body
        color: #fff
        a
            color: #fff
            &:hover
                color: #fff

.. code-block:: sass

    $color-green: #6cca4f;
    $padding: 20px;
    $width: 80%;

Миксины
-------


.. code-block:: sass

    =reset(){
        //
    }

    // вызов миксина
    +reset()
    .wrapper
        +wrapper()
    .parent
        .child
            +row-flex()
            +lg-block
                background-color: red;


scss
====

Блоки
-----

.. code-block:: scss

    body {
        color: #fff;
        a {
            color: #fff;
            &:hover {
                color: #fff;
            }
        }
    }


Импорт
------

Импорт, это не отдельный http запрос, а просто вставка данных из файла

.. code-block:: scss

    // импортируем файл _module.scss
    @import 'module';


Миксины
-------

.. code-block:: scss

    // миксин
    @mixin reset(){
        //
    }
    @mixin box-sizing{
        box-sizing: border-box;
    }
    @mixin border-radius($radius) {
        border-radius: $radius;
    }

    // вызов миксина
    @include wrapper;
    @include reset();
    @include debug(@key, @value);
    @include some-block{
        padding: 3px;
        margin-left: #{calc(#{$value} + #{value})};
    };
    .block {
        padding: $padding;
        border: 1px solid $color-green;
        width: $width/2 - 2%;

        color: darken(#4b6ef2, 40%);

        @include box-sizing;

        @include border-radius(10px);
    }

Переменные
----------

.. code-block:: scss

    $key: "some-key";
    $val: 12px;
    $color-green: #6cca4f;
    $padding: 20px;
    $width: 80%;

Расширения
----------

.. code-block:: scss

    %myStyle {
        color: #fff;
    }

    body {
        @extend %myStyle;
    }