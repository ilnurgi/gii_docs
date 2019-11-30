.. title:: pyqt4

.. meta::

    :description:
        Справочная информация по python модулю pyqt4, кросплатформенный фреймворк для построения графического интерфейса программ.
    :keywords:
        python pyqt4


.. py:module:: PyQt4

pyqt4
=====

https://doc.qt.io

Кросплатформенный фреймворк для построения графического интерфейса программ.

Существует две версии моудля pyqt4 b pyqt5.

pyqt4 работает как с qt 4 версии, так и с qt 5 версии.
pyqt5 работает работает только 5 версией qt.

.. code-block:: py

    import sys

    from PyQt4 import QtGui

    app = QtGui.QApplication(sys.argv)

    window = QtGui.QWidget()
    window.show()
    sys.exit(app.exec_())


Содержит следующие модули:

.. toctree::
   :maxdepth: 1

   phonon/index
   qaxcontainer/index
   qtcore/index
   qtdeclarative/index
   qtdesigner/index
   qtest/index
   qtgui/index
   qthelp/index
   qtmultimedia/index
   qtnetwork/index
   qtopengl/index
   qtscript/index
   qtscripttools/index
   qtsql/index
   qtsvg/index
   qtwebkit/index
   qtxml/index
   qtxmlpatterns/index
   uic/index
