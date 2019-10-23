.. title:: pyqt

.. meta::
    :description: 
      Справочная информация по модулю PyQt написанный для python.
    :keywords: 
      pyqt

.. py:module:: pyqt

pyqt
====

Кросплатформенный фреймворк

https://doc.qt.io

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
   qtwidgets/index
   qtxml/index
   qtxmlpatterns/index
   uic/index