.. title:: pyqt5

.. meta::

    :description:
        Справочная информация по python модулю PyQt5, кросплатформенный фреймворк для построения графического интерфейса программ.
    :keywords:
        python PyQt5


.. py:module:: PyQt5

PyQt5
=====

https://doc.qt.io

Кросплатформенный фреймворк для построения графического интерфейса программ.

Существует две версии моудля pyqt4 b pyqt5.

pyqt4 работает как с qt 4 версии, так и с qt 5 версии.
pyqt5 работает работает только 5 версией qt.

.. code-block:: py

    import sys

    from PyQt5.QtWidgets import QApplication, QWidget

    app = QApplication(sys.argv)

    window = QWidget()
    window.show()

    sys.exit(app.exec_())


Содержит следующие модули:

.. toctree::
    :maxdepth: 1

    qtcore/index
    qtwidgets/index
