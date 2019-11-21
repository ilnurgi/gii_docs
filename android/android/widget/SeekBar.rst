.. title:: android.widget.SeekBar

.. meta::
    :description:
        Справочная информация по android классу android.widget.SeekBar.
    :keywords:
        android widget SeekBar

.. py:currentmodule:: android.widget

SeekBar()
=========

.. code-block:: xml

    <SeekBar
        android:layout_height="wrap_content"
        android:layout_width="match_parent"
        android:layout_marginTop= "20dp"

        android:max="100"
        android:progress="50"
        android:id= "@+id/sbWeight" />

* id - идентификатор элемента

* max - максимальное значение

* progress - текущее значение

.. py:class:: SeekBar()

    .. code-block:: java

        SeekBar seekBar = (SeekBar) findViewById(R.id.seekBar);


    .. py:method:: getMax()

        Возвращает int, максимальное значение виджета

        .. code-block:: java

            int max = seekBar.getMax();


    .. py:method:: setOnSeekBarChangeListener(listener)

        Устанавливает обработчик изменения состояния

        * listener - должен реализовывать интерфейс :py:class:`android.widget.SeekBar.OnSeekBarChangeListener`

    .. py:class:: OnSeekBarChangeListener()

        Интерфейс, реализующий обработчик изменения


        .. py:method:: onProgressChanged(SeekBar seekBar, int progress, boolean fromUser)

            * seekbar - :py:class:`android.widget.SeekBar`


        .. py:method:: onStartTrackingTouch(SeekBar seekBar)

            * seekbar - :py:class:`android.widget.SeekBar`


        .. py:method:: onStopTrackingTouch(SeekBar seekBar)

            * seekbar - :py:class:`android.widget.SeekBar`
