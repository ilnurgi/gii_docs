.. title:: PySide2

.. meta::
    :description: PySide2
    :keywords: PySide2

.. py:module:: PySide2

PySide2
=======

https://www.qt.io/

.. toctree::
   :maxdepth: 1

   qtwidgets/index

.. code-block:: py

    import sys

    from PySide2.QtWidgets import QApplication, QLabel
     
    app = QApplication([])
    label = QLabel("Qt for Python!")
    label.show()
    sys.exit(app.exec_())
