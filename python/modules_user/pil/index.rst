.. title:: python pil

.. meta::
    :description:
        Справочная информация по python библиотеке pil.
    :keywords:
        python pil

.. py:module:: pil

pil
===

.. code-block:: py

    from pil import Image, ImageDraw, ImageFont

    image = Image.open('image.jpg')

    image.format
    # JPEG

    image.size
    # (200, 600)

    image.mode
    # RGB

    font = ImageFont.truetype('arial.ttf', 18)

    image_draw = ImageDraw.Draw(image)
    image_drw.text((10, 10), 'text', fill=(0, 0, 0), font=font)

    image.show()

.. code-block:: py

    from pil import Image, ImageFilter

    img1 = Image.open('img1.jpg')
    img2 = Image.open('img2.jpg')

    # наложение с прозрачностью
    Image.blend(img1, img2, 0.5).show()

    # чернобелое преобразование
    img1.convert('L').show()

    # чернобелый пиксели
    img1.convert('1').show()

    # размытие
    img1.filter(ImageFilter.BLUR).show()
    img1.filter(ImageFilter.CONTOUR).show()

    w, h = img1.size
    img1.getcolors(w*h)
    # (1, (0, 0, 0))

    img1.getpixel((100, 100))
    # (0, 0, 0)

    img1.getdata()
