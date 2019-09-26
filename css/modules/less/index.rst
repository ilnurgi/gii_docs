Less
====

Блоки, вложенность
------------------

.. code-block:: text

    .myClass {
        color: #fff;
    }

    body {
        .myClass;

        a {
            &:hover {
                color: #fff;
            }
        }
    }

Миксины
-------

.. code-block:: text

    /* миксин */
    .mixin(){
        display: flex;
    }
    .mixin(@name, @value){
        @{name}: @value;
    }
    .mixin-block(@content) {
        @media {
            @content;
        }
    }

    /* вложенность и вызов миксина */
    .row {
        @media {
            display: flex;
        }

        .column {
            color: @red;
            width: ~"calc(100% - @{size})";
        }

        &:hover {
            color: black;
        }

        &-column {
            color: red;
        }

        .mixin();
        .mixin(order, 0);
        .mixin-block({
            order: 0
        });
    }

Переменные
----------

.. code-block:: less

    @red: #0ff;

    body {
        color: @red;
    }


Сборка через gulp
-----------------

.. code-block:: sh

    npm install gulp-less

.. code-block:: js

    const gulp = require('gulp');
    const less = require('gulp-less');
    const rename = require('gulp-rename');
    const clean_css = require('gulp-clean-css');
    const del = require('del');

    paths = {
        styles: {
            src: 'src/**/*.less',
            dest: 'assets/styless/'
        }
    }

    // очистка папки ассетов
    const clean = () => del(['assets']);

    function styles(){
        return gulp
            .src(paths.styles.src)
            // преобразование в css
            .pipe(less())
            // очистка css
            .pipe(clean_css())
            // переименование
            .pipe(rename({
                basename: 'main',
                suffix: '.min'
            }))
            .pipe(gulp.dest(paths.styles.dest));
    }

gulp.task('default', gulp.series(clean, styles));