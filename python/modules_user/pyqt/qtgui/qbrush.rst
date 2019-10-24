.. title:: pyqt qtgui qbrush

.. meta::
    :description: 
        Справочная информация по модулю PyQt.QtGui.QBrush.
    :keywords: 
        pyqt qtgui qbrush

.. py:currentmodule:: PyQt.QtGui

QBrush
======

.. py:class:: QBrush()

    Кисть для рисования

    * `цвет` - атрибуты из класса :py:class:`QtCore.Qt`, или :py:class:`QtGui.QColor`

    * `qpixmap` - изображение, :py:class:`QtGui.QPixmap`

    * `qimage` - изображение

    .. code-block:: py

        * QBrush(<стиль>)
        * QBrush(<цвет>, <стиль>=SolidPattern)
        * QBrush(<цвет>, qpixmap)
        * QBrush(qpixmap)
        * QBrush(qimage)


    .. py:method:: setColor(color)

        Устанавливает цвет кисти

        * color - :py:class:`PyQt.QtGui.QColor`

        .. code-block:: py

            brush.setColor(QtGui.QColor('black'))


    .. py:method:: setStyle(style)

        Устанавливает стиль кисти

        * :py:attr:`PyQt.QtCore.Qt.CrossPattern` - текстура в виде сетки
        * :py:attr:`PyQt.QtCore.Qt.Dense1Pattern` -
        * :py:attr:`PyQt.QtCore.Qt.Dense2Pattern` -
        * :py:attr:`PyQt.QtCore.Qt.Dense3Pattern` -
        * :py:attr:`PyQt.QtCore.Qt.Dense4Pattern` -
        * :py:attr:`PyQt.QtCore.Qt.Dense5Pattern` -
        * :py:attr:`PyQt.QtCore.Qt.Dense6Pattern` -
        * :py:attr:`PyQt.QtCore.Qt.Dense7Pattern` -
        * :py:attr:`PyQt.QtCore.Qt.NoBrush` -
        * :py:attr:`PyQt.QtCore.Qt.SolidPattern` - сплошной

        .. code-block:: py

            brush.setStyle(Qt.SolidPattern)
