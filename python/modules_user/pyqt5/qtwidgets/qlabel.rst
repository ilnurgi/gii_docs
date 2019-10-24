.. title:: pyqt5 qwidgets qlabel

.. meta::

    :description:
        Справочная информация по python модулю PyQt5.QWidgets.QLabel.
    :keywords:
        python pyqt5 qlabel


.. py:currentmodule:: PyQt5.QWidgets

QLabel
======

.. py:class:: QLabel()

    .. code-block:: py

        label = QLabel('hello world', parent=window)

    .. py:method:: move(x, y)

        .. code-block:: py

            label.move(60, 15)


    .. py:method:: setText(text)

        Устаналивает текст виджета

        .. code-block:: py

            label.setText('ilnurgi')


    .. py:method:: text()

        Возвращает текст виджета

        .. code-block:: py

            label.text()
            # 'ilnurgi'
