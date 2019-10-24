.. title:: pyqt qtgui qpainter

.. meta::
    :description: 
      Справочная информация по модулю PyQt.QtGui.QPainter.
    :keywords: 
      pyqt qtgui qpainter

.. py:currentmodule:: PyQt.QtGui

QPainter
========

.. py:class:: QPainter()

    
    .. py:attribute:: device


    .. py:method:: device()

        Возвращает :py:class:`PyQt.GtGui.QPaintDevice`

        .. code-block:: py

            device = painter.device()


    .. py:method:: drawText(x, y, text)

        .. code-block:: py

            painter.drawText(25, 25, 'hello world')

    .. py:method:: end()


    .. py:method:: fillRect(rect, brush)

        * rect - :py:class:`PyQt.QtCore.QRect`
        * brush - :py:class:`PyQt.QtGui.QBrush`


    .. py:method:: font()

        Возвращает :py:class:`PyQt.QtGui.QFont`

        .. code-block:: py

            font = painter.font()


    .. py:method:: pen()

        Возвращает :py:class:`PyQt.QtGui.QPen`

        .. code-block:: py

            pen = painter.pen()


    .. py:method:: setFont(font)

        * font - :py:class:`PyQt.QtGui.QFont`

        .. code-block:: py

            painter.setFont(font)


    .. py:method:: setPen(pen)

        * pen - :py:class:`PyQt.QtGui.QPen`

        .. code-block:: py

            painter.setPen(pen)
