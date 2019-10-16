.. title:: html

.. meta::
    :description: 
        Описание языка разметки веб страниц html
    :keywords: 
        html

HTML
====

HTML - декларативный язык программирования,
используемый для разметки web-страниц - html-документов.

Web-страница отобржается в браузере (chrome, firefox, opera).

HTML документ состоит из тегов.

Тег - элемент разметки, который может иметь атрибуты.
Внутри тега может находиться обычный текст или другие теги.

.. code-block:: html

    <div></div>

    <!-- тег с атрибутом -->
    <тег атрибут=значение>
        <!--тут содержимое элемента-->

        <!--простой тег без атрибута-->
        <тег2>
            обычный текст
        </тег>

        <!--обычный текст-->
        другой текст

        <!--закрывающий тег, т.е. конец элемента-->
    </тег>


.. code-block:: html
   
    <!DOCTYPE>

    <html>

        <head>
            <meta charset="utf-8" />
            <title>Title</title>
        </head>

        <body>
            <!-- тело страницы -->
        </body>

    </html>


Элементы, описывающие документ
------------------------------

.. toctree::
    :maxdepth: 1

    html
    head
    link
    body
    doctype


Элементы, описывающие секции/блоки
----------------------------------

.. toctree::
    :maxdepth: 1

    article
    aside
    blockquote
    div
    em
    figure
    header
    img
    main
    nav
    picture
    section
    time


Элементы, описывающие списки
----------------------------

.. toctree::
    :maxdepth: 1

    dl
    ol
    ul



Элементы, описывающие текст
---------------------------

.. toctree::
    :maxdepth: 1

    a
    text
    p


Элементы, описывающие формы
---------------------------

.. toctree::
    :maxdepth: 1

    form
    input
    datalist


.. toctree::
    :maxdepth: 2

    html5/index
    doc
    mnemonic
    table
    text


Шаблонизаторы
-------------

.. toctree::
    :maxdepth: 1

    pug


code
----

Фрагмент кода


embed
-----

.. note:: HTML5

Внедрение объекта на страницу

* height - высота элемента

* src - ссылка на ресурс

* type - тип ресурса

* width - ширина элемента

.. code-block:: html

    <embed src="ilnurgi.mov" width="240" height="320" type="video/quicktime"


iframe
------

Фрейм, используемый для внедрения другого документа

* allowfullscreen

    .. note:: HTML5

* height - высота элемента

* sandbox

    .. note:: HTML5

    * allow-forms

    * allow-pointer-lock

    * allow-popups

    * allow-same-origin

    * allow-scripts

    * allow-top-navigation

* seamless

    .. note:: HTML5

* src

* srcdoc

    .. note:: HTML5

* width - ширина элемента

.. code-block:: html

    <iframe src="ads.html" width="320" height="240"></iframe>

svg
---

Способы подключения

.. code-block:: html

    <svg> <!--SVG content--> </svg>

    <img  src="logo.svg" alt="Company Logo">

    <object type="image/svg+xml" data="logo.svg">
        <!--содержимое, если logo.svg недоступно-->
    </object>

    <iframe src="logo.svg">
        <!--содержимое, если logo.svg недоступно-->
    </iframe>



.. code-block:: css

    .element {
        background: url(logo.svg);
    }
