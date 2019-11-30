.. title:: android.widget.AbsoluteLayout

.. meta::
    :description:
        Справочная информация по android классу android.widget.AbsoluteLayout.
    :keywords:
        android widget AbsoluteLayout

.. py:currentmodule:: android.widget

AbsoluteLayout()
================

Контейнер, который распологает элементы по абсолютным значениям

.. code-block:: xml

    <AbsoluteLayout
        xmlns:android="http://schemas.android.com/apk/res/android"

        android:layout_width="match_parent"
        android:layout_height="match_parent" >

        <Button

            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_x="42dp"
            android:layout_y="62dp"

            android:text="Button"
            android:id="@+id/button1" />

    </AbsoluteLayout>

* **layout_height** - высота элемента

    * **match_parent** - заполнить родителя

    * **wrap_content** - по содержимому

* **layout_width** - ширина элемента

    * **match_parent** - заполнить родителя

    * **wrap_content** - по содержимому

* **layout_x** - абсолютная координата расположения элемента

* **layout_y** - абсолютная координата расположения элемента

.. py:class:: AbsoluteLayout()

    Наследник :py:class:`android.view.ViewGroup`

    .. py:class:: android.widget.AbsoluteLayout.LayoutParams

        Настройки слоя

        Наследник :py:class:`android.view.ViewGroup.LayoutParams`
