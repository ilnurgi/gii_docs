.. title:: css media

.. meta::
    :description: 
        Описание элемента media каскадных стилей описания веб документов.
    :keywords: 
        css media

media
=====

Медиазапросы

Типы устройств:

* all - все устройства
* braille - устройства с тактильной обратной связью
* embossed - брайлевсике принтеры
* handled - портативные устройства
* print - принтеры
* projection - проекторы
* screen - цветные экраны
* speech - речевые синтезаторы
* tty - моноширинная символьная среда
* tv - телевизоры

Другие:

* color - количество бит на цвет
* color-index - количесвто записей в таблице подстановки цветов
* grid - устройство с фиксированным размером символов
* monochrome - сколько бит на каждый пиксель
* orientation - ориентация экрана
* resolution - разрешение экрана или печати
* scan - тип развертки
* width - ширина области просмотра
* height - высота области просмотра
* min-width
* max-width
* min-height
* max-height
* device-width - ширина экрана
* device-height - высота экрана
* min-device-width
* max-device-width
* min-device-height
* max-device-height
* aspect-ratio - соотношение сторон области просмотра
* min-aspect-ratio
* max-aspect-ratio
* device-aspect-ratio - соотношение сторон экрана
* min-device-aspect-ratio
* max-device-aspect-ratio

.. code-block:: css
    
    @media screen and (max-width: 960px){}

    /* Desktops 1281px или больше */
    @media (min-width: 1281px) {}

    /* Laptops, Desktops между 1025px и 1280px */
    @media (min-width: 1025px) and (max-width: 1280px) {}

    /* Tablets, Ipads (portrait) между 768px и 1024px */
    @media (min-width: 768px) and (max-width: 1024px) {}

    /* Tablets, Ipads (landscape) между 768px и 1024px */
    @media (min-width: 768px) and (max-width: 1024px) and (orientation: landscape) {}

    /* Low Resolution Tablets, Mobiles (Landscape) между 481px и 767px */
    @media (min-width: 481px) and (max-width: 767px) {}

    /* Most of the Smartphones Mobiles (Portrait) между 320px и 479px */
    @media (min-width: 320px) and (max-width: 480px) {}
    