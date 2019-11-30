.. title:: html.picture

.. meta::
    :description: html.picture
    :keywords: html.picture

picture
=======

source
------

.. code-block:: html

    <picture>
        <source 
            media="(min-width: 600px) and (max-width: 1200px)"
            srcset="images/ilnurgi-medium.jpg"
        >
        <source 
            media="(min-width: 1201px)"
            srcset="images/ilnurgi-large.jpg"
        >
        <img src="images/ilnurgi.jpg" alt="ilnurgi face">
    </picture>

.. code-block:: html
    
    <-- изображение будет использоваться в зависимости от поддержки браузера -->
    <picture>
        <source 
            type="image/svg+xml"
            srcset="ilnurgi.svg"
        >
        <source 
            type="image/webp"
            srcset="ilnurgi.webp"
        >
        <img src="images/ilnurgi.jpg" alt="ilnurgi face">
    </picture>