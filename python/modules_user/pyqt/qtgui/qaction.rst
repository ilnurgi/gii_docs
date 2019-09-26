QAction
=========


.. py:class:: QAction()

    .. code-block:: py

        self.lineEdit = QtGui.QLineEdit()
        self.act = QtGui.QAction(self)
        self.act.setShortcut(QtGui.QKeySequence.mnemonic("&e"))
        self.act.triggered.connect(self.lineEdit.setFocus)
        self.addAction(self.act)
