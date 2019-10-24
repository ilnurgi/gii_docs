.. title:: pyqt5 qtwidgets qdial

.. meta::
    :description:
      Справочная информация по объекту PyQt5.QtWidgets.QDial.
    :keywords:
      pyqt5 qtwidgets qdial

.. py:currentmodule:: PyQt5.QtWidgets

QDial
=====

.. py:class:: QDial()

    .. figure:: images/qdial.png

    .. code-block:: py

        dial = QDial()
        dial.valueChanged.connect(callback)


    .. py:attribute:: valueChanged

        Обработчик изменения значения

        .. code-block:: py

            dial.valueChanged.connect(callback)


    .. py:method:: minimum()

        .. code-block:: py

            minimum = qdial.minimum()


    .. py:method:: maximum()

        .. code-block:: py

            maximum = qdial.maximum()
