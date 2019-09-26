pug
---

pugjs.org

.. code-block:: text

    // include config.pug подключить переменные из файла
    - var lang = 'en'
    - var myTitle = 'Title'

    // layout.pug

    doctype html
    // doctype xml
    
    html(lang=lang)
        head
            meta(charset="utf-8")
            meta(name="viewport" content="width=device-width, initial-scale=1.0")
            title #{myTitle}
            link(rel="stylesheet" href="/styles.css")
        body
            include header.pug
            ul
                li: a(href="#") Link
                li
                    a(href="#") Link
            p#id.class1.class2
                | много строк
                | много строк
                | 
                    a(href="#") Якорь
                | .
            p.
                много строк
                много строк

            p(class=['class1', 'class2']) Привет, #[em мир]!
            a&attributes({
                'target': '_blank',
            }) Доп атрибуты

            block main
                Содержимое по умолчанию

            script.
                // далее js скрипт
                document.getElementById('root')

            style
                h1 {
                    font-size: 100px;
                }

            style
                :scss
                    // фильтры
                    ul {
                        li {}
                    }

.. code-block:: pug

    // main.pug
    extends layout

    // append main - добавление элементов после по умолчанию
    // prepend main - добавление элементов до по умолчанию

    block main // заменит сожержимое по умолчанию

        h1 Hello World
        form(method="POST")
            input(type="text" name="username")
            button(type="submit") Войти

        ul
            for item in items
                li #{item}
                li=item
                li=item.title |  (#{item.counter} просмотров)


        if username
            h1 Hello #{username}
        else
            h1 Hello anonimus