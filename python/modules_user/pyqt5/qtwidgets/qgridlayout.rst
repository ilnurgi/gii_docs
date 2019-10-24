.. title:: pyqt5 qwidgets qgridlayout

.. meta::

    :description:
        Справочная информация по python объекту PyQt5.QWidgets.QGridLayout.
    :keywords:
        python pyqt5 qgridlayout


.. py:currentmodule:: PyQt5.QWidgets

QGridLayout
===========

.. py:class:: QGridLayout()

    .. code-block:: py

        layout = QGridLayout()

    .. py:method:: addWidget(widget, row, columnt, row_span=1, column_span=1)

        .. code-block:: py

            layout.addWidget(QPushButton('Left'), 0, 0)
            layout.addWidget(QPushButton('Right'), 0, 1)
            layout.addWidget(QPushButton('Span 2 columns'), 1, 0, 1, 2)
