.. title:: android.widget.Spinner

.. meta::
    :description:
        Справочная информация по android классу android.widget.Spinner.
    :keywords:
        android widget Spinner

.. py:currentmodule:: android.widget

Spinner()
=========

.. code-block:: xml

    <Spinner
        android:id="@+id/spinner"
        android:layout_width="match_parent"
        android:layout_height="wrap_content">
    </Spinner>

.. py:class:: Spinner()

    Составной элемент, отображающий TextView
    в сочетании с соответствующим представлением ListView,
    которое позволяет выбрать элемент списка для отображения в текстовой строке.

    Сама строка состоит из объекта TextView, показывающего текущий выбор,
    и кнопки, при нажатии которой всплывает диалог выбора.

    Наследник :py:class:`android.view.View`

    .. code-block:: java

        Spinner spinner = (Spinner) findViewById(R.id.spinner);


    .. py:method:: getSelectedItem()


    .. py:method:: getSelectedItemPosition()

        Возвращает позицию выделенного элемента


    .. py:method:: setAdapter(ArrayAdapter adapter)

        Устанавливает адаптер


    .. py:method:: setOnItemSelectedListener(OnItemSelectedListener listener)

        Устанавливает слушателя выбора элемента

        * listener - :py:class:`android.widget.AdapterView.OnItemSelectedListener`


    .. py:method:: setPrompt(String prompt)

        Заголовок


    .. py:method:: setSelection(int pos)

        Выделяет элемент

