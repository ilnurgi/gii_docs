Element
=======

Элемент узла дом дерева

.. py:class:: Element()

    Наследник :py:class:`Node`

    .. py:attribute:: className

        Это свой­ст­во пред­став­ля­ет ат­ри­бут class эле­мен­та.

    .. py:method:: insertAdjacentElement(position, element)

        * position - позиция добавляемого элемента

            * beforebegin - до самого element (до открывающего тега)
            * afterbegin - сразу после открывающего тега  element (перед первым потомком)
            * beforeend - сразу перед закрывающим тегом element (после последнего потомка)
            * afterend - после element (после закрывающего тега)

        Добавляет переданный элемент в DOM-дерево относительно элемента, вызвавшего метод и возвращает его.


    .. py:method:: matches(selectorString);

        Возвращает булево, удовлетворяет ли элемент селектору

        .. code-block:: js

            elem.matches('.some-class');
            // true


HTMLAnchorElement
-----------------

Элемент `<a>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLAnchorElement

    .. py:attribute:: href

    .. py:attribute:: target

    .. py:attribute:: ping

    .. py:attribute:: rel

    .. py:attribute:: media

    .. py:attribute:: hreflang

    .. py:attribute:: type


HTMLAppletElement
-----------------

Элемент `<applet>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLAppletElement


HTMLAreaElement
---------------

Элемент `<area>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLAreaElement

    .. py:attribute:: alt

    .. py:attribute:: coords

    .. py:attribute:: shape

    .. py:attribute:: href

    .. py:attribute:: target

    .. py:attribute:: ping

    .. py:attribute:: rel

    .. py:attribute:: media

    .. py:attribute:: hreflang

    .. py:attribute:: type


HTMLBaseElement
---------------

Элемент `<base>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLBaseElement

    .. py::attribute:: href

    .. py::attribute:: target


HTMLBaseFontElement
-------------------

Элемент `<basefont>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLBaseFontElement


HTMLBodyElement
---------------

Элемент `<blockquote>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLBodyElement

    .. py:attribute:: onafterprint

    .. py:attribute:: onbeforeprint

    .. py:attribute:: onbeforeunload

    .. py:attribute:: onblur

    .. py:attribute:: onerror

    .. py:attribute:: onfocus

    .. py:attribute:: onhash­

    .. py:attribute:: change

    .. py:attribute:: onload

    .. py:attribute:: onmessage

    .. py:attribute:: onoffline

    .. py:attribute:: ononline

    .. py:attribute:: onpagehide

    .. py:attribute:: onpage­show

    .. py:attribute:: onpopstate

    .. py:attribute:: onredo

    .. py:attribute:: onresize

    .. py:attribute:: onscroll

    .. py:attribute:: onstorage

    .. py:attribute:: onundo

    .. py:attribute:: onunload


HTMLButtonElement
-----------------

Элемент `<button>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLButtonElement

    .. py:attribute:: autofocus

    .. py:attribute:: disabled

    .. py:attribute:: form

    .. py:attribute:: formaction

    .. py:attribute:: formenctype

    .. py:attribute:: formmethod

    .. py:attribute:: form­nova­

    .. py:attribute:: lidate

    .. py:attribute:: formtarget

    .. py:attribute:: name

    .. py:attribute:: type

    .. py:attribute:: value


HTMLBRElement
-------------

Элемент `<br>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLBRElement


HTMLDListElement
----------------

Элемент `<dl>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLDListElement


HTMLDirectoryElement
--------------------

Элемент `<dir>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLDirectoryElement


HTMLDivElement
--------------

Элемент `<div>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLDivElement


HTMLFieldSetElement
-------------------

Элемент `<fieldset>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLFieldSetElement

    .. py:attribute:: disabled
    
    .. py:attribute:: form
    
    .. py:attribute:: name


HTMLFontElement
---------------

Элемент `<font>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLFontElement


HTMLFormElement
---------------

Элемент `<from>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLFormElement

    .. py:attribute:: accept-charset

    .. py:attribute:: action

    .. py:attribute:: autocomplete
    
    .. py:attribute:: elements
    
    .. py:attribute:: enctype
    
    .. py:attribute:: method
    
    .. py:attribute:: name
    
    .. py:attribute:: novalidate
    
    .. py:attribute:: target

    .. py:attribute:: length

    .. py:function:: submit()

    .. py:function:: reset()

HTMLFrameElement
----------------

Элемент `<frame>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLFrameElement


HTMLFrameSetElement
-------------------

Элемент `<frameset>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLFrameSetElement


HTMLHeadElement
---------------

Элемент `<head>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLHeadElement


HTMLHeadingElement
------------------

Элемент `<h1> ... <h6>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLHeadingElement


HTMLHtmlElement
---------------

Элемент `<html>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLHtmlElement

    .. py:attribute:: manifest


HTMLHRElement
-------------

Элемент `<hr>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLHRElement


HTMLImageElement
----------------

Элемент `<image>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLImageElement

    .. py:attribute:: alt
    
    .. py:attribute:: src
    
    .. py:attribute:: usemap
    
    .. py:attribute:: ismap
    
    .. py:attribute:: width
    
    .. py:attribute:: height


HTMLInputElement
----------------

Элемент `<input>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLInputElement

    .. py:attribute:: accept

    .. py:attribute:: alt

    .. py:attribute:: autocomplete

    .. py:attribute:: autofocus

    .. py:attribute:: checked

    .. py:attribute:: defaultChecked
    
    .. py:attribute:: defaultValue

    .. py:attribute:: dirname

    .. py:attribute:: disabled

    .. py:attribute:: form

    .. py:attribute:: form­

    .. py:attribute:: ac­tion

    .. py:attribute:: formenctype

    .. py:attribute:: formmethod

    .. py:attribute:: formnovalidate

    .. py:attribute:: formtarget

    .. py:attribute:: height

    .. py:attribute:: list

    .. py:attribute:: max

    .. py:attribute:: maxlength

    .. py:attribute:: min

    .. py:attribute:: multiple

    .. py:attribute:: name

    .. py:attribute:: pattern

    .. py:attribute:: placeholder

    .. py:attribute:: readonly

    .. py:attribute:: required

    .. py:attribute:: size

    .. py:attribute:: src

    .. py:attribute:: step

    .. py:attribute:: type

    .. py:attribute:: value

    .. py:attribute:: width

    .. py:function:: blur()

    .. py:function:: click()

    .. py:function:: focus()

    .. py:function:: select()


HTMLIsIndexElement
------------------

Элемент `<isindex>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLIsIndexElement


HTMLIFrameElement
-----------------

Элемент `<iframe>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLIFrameElement

    .. py:attribute:: src
    
    .. py:attribute:: srcdoc
    
    .. py:attribute:: name
    
    .. py:attribute:: sandbox
    
    .. py:attribute:: seamless
    
    .. py:attribute:: width
    
    .. py:attribute:: height


HTMLLabelElement
----------------

Элемент `<label>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLLabelElement

    .. py:attribute:: form
    
    .. py:attribute:: for


HTMLLegendElement
-----------------

Элемент `<legend>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLLegendElement


HTMLLinkElement
---------------

Элемент `<li>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLLinkElement

    .. py:attribute:: href

    .. py:attribute:: rel

    .. py:attribute:: media

    .. py:attribute:: hreflang

    .. py:attribute:: type

    .. py:attribute:: sizes


HTMLLIElement
-------------

Элемент `<li>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLLIElement

    .. py:attribute:: value


HTMLMapElement
--------------

Элемент `<map>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLMapElement

    .. py:attribute:: map


HTMLMenuElement
---------------

Элемент `<menu>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLMenuElement

    .. py:attribute:: type

    .. py:attribute:: label


HTMLMetaElement
---------------

Элемент `<meta>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLMetaElement

    .. py:attribute:: name
    
    .. py:attribute:: http-equiv
    
    .. py:attribute:: content
    
    .. py:attribute:: charset


HTMLModElement
--------------

Элемент `<del>`, `<ins>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLModElement

    .. py:attribute:: cite

    .. py:attribute:: datetime


HTMLObjectElement
-----------------

Элемент `<object>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLObjectElement

    .. py:attribute:: data
    
    .. py:attribute:: type
    
    .. py:attribute:: name
    
    .. py:attribute:: usemap
    
    .. py:attribute:: form
    
    .. py:attribute:: width
    
    .. py:attribute:: height


HTMLOptGroupElement
-------------------

Элемент `<optgroup>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLOptGroupElement

    .. py:attribute:: disabled

    .. py:attribute:: label


HTMLOptionElement
-----------------

Элемент `<option>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLOptionElement

    .. code-block:: js

        var o = new Option(text, value, defaultSelected, selected);

    .. py:attribute:: form

    .. py:attribute:: defaultSelected

    .. py:attribute:: disabled
    
    .. py:attribute:: index

    .. py:attribute:: label
    
    .. py:attribute:: selected

    .. py:attribute:: text

    .. py:attribute:: value


HTMLOListElement
----------------

Элемент `<ol>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLOListElement

    .. py:attribute:: reversed

    .. py:attribute:: start


HTMLParagraphElement
--------------------

Элемент `<p>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLParagraphElement

    .. py:attribute:: cite


HTMLParamElement
----------------

Элемент `<param>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLParamElement

    .. py:attribute:: name
    
    .. py:attribute:: value


HTMLPreElement
--------------

Элемент `<pre>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLPreElement


HTMLQuoteElement
----------------

Элемент `<q>`, `<blockquote>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLQuoteElement

    .. py:attribute:: cite


HTMLScriptElement
-----------------

Элемент `<script>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLScriptElement

    .. py:attribute:: src
    
    .. py:attribute:: async
    
    .. py:attribute:: defer
    
    .. py:attribute:: type
    
    .. py:attribute:: charset


HTMLSelectElement
-----------------

Элемент `<select>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLSelectElement

    .. py:attribute:: autofocus

    .. py:attribute:: disabled

    .. py:attribute:: form

    .. py:attribute:: length

    .. py:attribute:: multiple

    .. py:attribute:: name

    .. py:attribute:: options

    .. py:attribute:: required

    .. py:attribute:: selectedIndex

    .. py:attribute:: size

    .. py:attribute:: tabIndex

    .. py:attribute:: type

    .. py:attribute:: value

    .. py:function:: add()

    .. py:function:: blur()

    .. py:function:: focus()

    .. py:function:: remove()


HTMLStyleElement
----------------

Элемент `<select>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLStyleElement

    .. py:attribute:: media
    
    .. py:attribute:: type
    
    .. py:attribute:: scoped


HTMLTableCaptionElement
-----------------------

Элемент `<caption>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLTableCaptionElement



HTMLTableColElement
-------------------

Элемент `<col>`, `<colgroup>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLTableColElement

    .. py:attribute:: span


HTMLTextAreaElement
-------------------

Элемент `<textarea>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLTextAreaElement

    .. py:attribute:: autofocus
    
    .. py:attribute:: cols
    
    .. py:attribute:: defaultValue

    .. py:attribute:: disabled
    
    .. py:attribute:: form
    
    .. py:attribute:: maxlength
    
    .. py:attribute:: name
    
    .. py:attribute:: placeholder
    
    .. py:attribute:: readonly
    
    .. py:attribute:: requi­r­ed
    
    .. py:attribute:: rows
    
    .. py:attribute:: tabIndex

    .. py:attribute:: type

    .. py:attribute:: value

    .. py:attribute:: wrap

    .. py:function:: blur()

    .. py:function:: focus()

    .. py:function:: select()


HTMLTitleElement
----------------

Элемент `<title>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLTitleElement


HTMLUListElement
----------------

Элемент `<ul>`

Наследник :py:class:`HTMLElement`

.. py:class:: HTMLUListElement


============ ========
Эле­мент      Ат­ри­бу­ты
============ ========
<audio>      src, preload, autoplay, loop, controls
<canvas>     width, height
<command>    type, label, icon, disabled, checked, radiogroup
<details>    open
<embed>      src, type, width, height
<keygen>     autofocus, challenge, disabled, form, keytype, name
<meter>      value, min, max, low, high, optimum, form
<output>     for, form, name
<progress>   value, max, form
<source>     src, type, media
<time>       datetime, pubdate
<track>      default, kind, label, src, srclang
<video>      src, poster, preload, autoplay, loop, controls, width, height
============ ========