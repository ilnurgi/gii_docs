.. title:: PySide2.QtWidgets.QDialog

.. meta::
    :description: PySide2.QtWidgets.QDialog
    :keywords: PySide2.QtWidgets.QDialog

.. py:module:: PySide2.QtWidgets

QDialog()
=========

.. py:class:: QDialog()

    .. code-block:: py

        class Form(QDialog):
         
            def __init__(self, parent=None):
                super(Form, self).__init__(parent)
         
                self.edit = QLineEdit("What's up?")
                self.button = QPushButton("Print to stdout")
         
                layout = QVBoxLayout()
                layout.addWidget(self.edit)
                layout.addWidget(self.button)
         
                self.setLayout(layout)
         
                self.button.clicked.connect(self.greetings)
         
         
            def greetings(self):
                text = self.edit.text()
                print('Contents of QLineEdit widget: {}'.format(text))

        app = QApplication([])
        form = Form()
        form.show()
        sys.exit(app.exec_())

    .. py:method:: setLayout(layout)

    .. py:method:: show()