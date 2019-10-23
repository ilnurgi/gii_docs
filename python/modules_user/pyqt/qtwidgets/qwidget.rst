.. title:: pyqt qtwidgets qwidget

.. meta::
    :description: 
      Справочная информация по модулю PyQt.QtWidgets.QWidget.
    :keywords: 
      pyqt qtwidgets qwidget

.. py:currentmodule:: PyQt.QtWidgets

QWidget
=======

.. py:class:: QWidget()
  
    .. py:method:: paintEvent(event)

        * event - :py:class:`QPaintEvent`

        .. code-block:: py

            def paintEvent(event):
                painter = QtGui.QPainter(self)
                painter.drawText(25, 25, 'hello world')
                painter.end()


    .. py:method:: repaint()

    
    .. py:method:: setSizePolicy()

        .. code-block:: py

            windget.setSizePolicy(
                QtWidgets.QSizePolicy.MinimumExpanding,
                QtWidgets.QSizePolicy.MinimumExpanding,
            )


    .. py:method:: update()