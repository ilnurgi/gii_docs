jade
====

.. code-block:: sh

    npm install jade

.. code-block:: text

    // header.jade
    doctype
    head
        title= page
        meta(charset='utf-8')
        link(rel='stylesheet' href='style.css')
        style
            ul.nav a{
                color: red;
            }
    body
        .container
            h1= page
            hr
            ul.nav.nav-pills
                each link in links
                    li: a(href=link)= link
            hr
        block content

    // index.jade
    extends header

    block content
        p= content

        .row
            .col-sm-3
                h2
                p
            .col.sm-9
                h2
                p

        hr
        form(method='post' action='/new')
            fieldset
                .form-group
                    label(for='page_url') Page Url
                    input#page_url.form-control(name='page_url' type='text')
                .form-group
                    button.btn.btn-primary(type='submit') Add