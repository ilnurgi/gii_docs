.. title:: pyqt

.. meta::
    :description: pyqt
    :keywords: pyqt

.. py:module:: pyqt

pyqt
====

Кросплатформенный фреймворк


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
   qt/index   
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