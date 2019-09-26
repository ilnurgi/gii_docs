QShortcut
=========


.. py:class:: QShortcut()

    .. code-block:: py

        self.lineEdit = QtGui.QLineEdit()
        self.shc = QtGui.QShortcut(QtGui.QKeySequence.mnemonic("&e"), self)
        self.shc.setContext(QtCore.Qt.WindowShortcut)
        self.shc.activated.connect(self.lineEdit.setFocus)
