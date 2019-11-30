.. title:: pyqt5 qwidgets qmainwindow

.. meta::

    :description:
        Справочная информация по python модулю PyQt5.QWidgets.QMainWindow.
    :keywords:
        python pyqt5 qmainwindow


.. py:currentmodule:: PyQt5.QWidgets

QMainWindow
===========

.. py:class:: QMainWindow()

    .. code-block:: py

        class MyMainWindow(QMainWindow):
            pass

    .. py:method:: addToolBar(tool_bar)

        * tool_bar - :py:class:`PyQt5.QWidgets.QToolBar`

        Добавляет панель инструментов окна

        .. code-block:: py

            my_window.addToolBar(QToolBar())


    .. py:method:: menuBar()

        Возвращает объект меню

        .. code-block:: py

            menu_bar = my_window.menuBar()

            menu_item = menu_bar.addMenu('&Menu')
            menu_item.addAction('&Exit', callback)


    .. py:method:: setCentralWidget(widget)

        Устанавливает центральный виджет

        .. code-block:: py

            my_window.setCentralWidget(QLabel('central widget'))


    .. py:method:: setFixedSize(w, h)

        Устанавливает фиксированные размеры окна


    .. py:method:: setWindowTitle(title)

        Устанавливает заголовок окна


    .. py:method:: show()

        Показывает окно в системе
