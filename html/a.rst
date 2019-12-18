.. title:: html a

.. meta::
    :description:
        Конспекты по html. Описание элемента a, ссылка в html документе.
    :keywords:
        html a

a
=

Якорь, гипертекстовая ссылка

Строчный элемент

.. code-block:: html

    <a>текст ссылки</a>

.. code-block:: html

    <a href="http:/ilnurgi.ru" id="my_anchor"></a>
    <a href="http:/ilnurgi.ru/post.html#news"></a>
    <a href="mailto:ilnurgi87@gmail.com"></a>
    <a href="tel:+1234567890"></a>

.. code-block:: html

    <a id="anchor_bottom"></a>
    <a href="#anchor_bottom"></a>


download
--------

Данная ссылка будет открыта не в новом окне, а будет скачана браузером.

.. note:: HTML5.1

.. code-block:: html

    <a href="img.png" download>Картинка</a>

    <!-- cat - имя сохраняемого файла -->
    <a href="img.png" download="cat">Картинка</a>


href
----

Адрес ресурса, куда ведет ссылка

.. code-block:: html

    <a href="http://ilnurgi1.ru">ilnurgi1.ru</a>
    <a href="mailto: mail@mail.rur">Почта</a>
    <a href="slack://open?team"></a>
    <a href="tel: +7..">Телефон</a>

.. code-block:: html

    <a href="#name">ilnurgi1.ru</a>

    <div id="name"></div>


hreflang
--------

Язык целевого документа

.. code-block:: html

    <a hreflang="ru"></a>

ping
----

.. code-block:: html

    <ahref="doc.pdf" ping="/ping"></a>


referrerpolicy
--------------

Управляет доступом к заголовку Referer

* **no-referrer**

.. code-block:: html

    <a href="" referrerpolicy="no-referrer"></a>


rel
---

Связь между исодным и связанными документами

* **alternate** 
* **author**
* **bookmark**
* **external**
* **help**
* **license**
* **next**
* **nofollow**
* **noopener**
* **noreferrer**
* **prefetch**
* **prev**
* **search**
* **tag**


target
------

Имя окна или области iframe, где будет открываться документ

* **_blank** - открыть в новой вкладке
* **_self** - открыть в текущем контексте
* **_parent** - открыть в родительском контексте
* **_top** - открыть в верхнем контексте
* **iframe-name** - открыть в контексте name="iframe-name"

* ****
.. code-block:: html

    <a href="http://ilnurgi1.ru" target="_blank">ilnurgi1.ru</a>
    <a href="http://ilnurgi1.ru" target="_self"></a>


title
-----

Добавляет всплывающую подсказу при наведении

.. code-block:: html

    <a href="http://ilnurgi1.ru" title="ссылка на мой проект">ilnurgi1.ru</a>


type
----

Тип контента для связанного контента

* **application/pdf**
* **text/html**

.. code-block:: html

    <a href="doc.pdf" type="application/pdf"></a>