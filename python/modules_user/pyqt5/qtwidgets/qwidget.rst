.. title:: pyqt qtwidgets qwidget

.. meta::
    :description:
      Справочная информация по python модулю PyQt5.QWidgets.QLabel.
    :keywords:
      pyqt qtwidgets qwidget

.. py:currentmodule:: PyQt.QtWidgets

QWidget
=======

.. py:class:: QWidget()

    .. code-block:: py

        window = QWidget()


    .. py:method:: move(x, y)

        .. code-block:: py

            window.move(60, 15)


    .. py:method:: paintEvent(event)

        * event - :py:class:`QPaintEvent`

        .. code-block:: py

            def paintEvent(event):
                painter = QtGui.QPainter(self)
                painter.drawText(25, 25, 'hello world')
                painter.end()


    .. py:method:: repaint()


    .. py:method:: setGeometry(x, y, w, h)

        .. code-block:: py

            window.setGeometry(100, 100, 280, 80)


    .. py:method:: setLayout(layout)

        .. code-block:: py

            window.setLayout(QHBoxLayout())


    .. py:method:: setSizePolicy()

        .. code-block:: py

            windget.setSizePolicy(
                QtWidgets.QSizePolicy.MinimumExpanding,
                QtWidgets.QSizePolicy.MinimumExpanding,
            )


    .. py:method:: setWindowTitle(title)

        .. code-block:: py

            window.setWindowTitle('PyQt5 App')

    .. py:method:: show()

        .. code-block:: py

            window.show()


    .. py:method:: update()
