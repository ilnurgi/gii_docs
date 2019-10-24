.. title:: pyqt5 qwidgets qpushbutton

.. meta::

    :description:
        Справочная информация по python модулю PyQt5.QWidgets.QPushButton.
    :keywords:
        python pyqt5 qpushbutton


.. py:currentmodule:: PyQt5.QWidgets

QPushButton
===========

.. py:class:: QPushButton()

    .. code-block:: py

        button = QPushButton('hello world', parent=window)

    .. py:attribute:: clicked

        Сигнал клика

        .. code-block:: py

            button.clicked.connect(callback)
            button.clicked.connect(functools.partial(callback, some_param))


    .. py:method:: setFixedSize(h, w)

        Устанавливает указанный размер виджета
