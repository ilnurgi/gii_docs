.. title:: html.img

.. meta::
    :description: html.img
    :keywords: html.img

img
===

Изображение

.. code-block:: html

    <img src='http://ilnurgi1.ru/img.png'>


alt
---

Альтернативный текст, отображается когда картинка ещё не загружена

.. code-block:: html

    <img src='http://ilnurgi1.ru/img.png' alt='описание не загруженной картинки'>


crossorigin
-----------

* anonymous
* use-credentials


height
------

высота элемента


ismap
-----


sizes
-----

Набор медиавыражений в размерами картинки для каждого условия

.. code-block:: html

    .. code-block:: html

        <-- 30vh размер картинки на условие max-width -->
        <-- 400px размер по умолчанию -->
        <img 
            src="ilnurgi-200px.jpg" 
            alt="ilnurgi face" 
            width="200"
            sizes="(max-width: 1000px) 30vh, 400px"
        >

        <img 
            src="ilnurgi-200px.jpg" 
            alt="ilnurgi face" 
            width="200"
            sizes="(max-width: 399px) 50vw,
                   (min-width: 400px) and (max-width: 900px) calc(30vh - 40px),
                   100vw"
        >

        <img 
            src="ilnurgi-200px.jpg" 
            alt="ilnurgi face" 
            width="200"
            srcset="ilnurgi-200px.jpg 200w, 
                    ilnurgi-400px.jpg 400w, 
                    ilnurgi-600px.jpg 500w"
            sizes="(max-width: 800px) 30vw, 600px"
        >

src
---

Ссылка на источник объекта

.. code-block:: html

    <img src='http://ilnurgi1.ru/img.png'>


srcset
------

Позволяет указать набор картинок

.. code-block:: html

    .. code-block:: html

        <-- 1x, .... 4x плотность экрана -->
        <img 
            src="ilnurgi-200px.jpg" 
            alt="ilnurgi face" 
            width="200"
            srcset="ilnurgi-200px.jpg 1x, 
                    ilnurgi-400px.jpg 2x, 
                    ilnurgi-600px.jpg 3x,
                    ilnurgi-800px.jpg 4x"
        >

        <img 
            src="ilnurgi-200px.jpg" 
            alt="ilnurgi face" 
            width="200"
            srcset="ilnurgi-200px.jpg 200w, 
                    ilnurgi-400px.jpg 400w, 
                    ilnurgi-600px.jpg 600w"
        >

usemap
------


width
-----

ширина элемента
