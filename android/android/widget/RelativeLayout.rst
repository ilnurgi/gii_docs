.. title:: android.widget.RelativeLayout

.. meta::
    :description:
        Справочная информация по android классу android.widget.RelativeLayout.
    :keywords:
        android widget RelativeLayout

.. py:currentmodule:: android.widget

RelativeLayout()
================

Контейнер, позволяет задавать позицию каждого дочернего элемента
относительного других элементов и границ экрана.

.. code-block:: xml

    <RelativeLayout
        xmlns:android="http://schemas.android.com/apk/res/android"

        android:layout_width="wrap_content"
        android:layout_height="wrap_content">

        <TextView
            android:id="@+id/label" />

        <TextView
            android:layout_below="@id/label"
            android:layout_alignParent="true"

            android:id="@+id/label2" />

    </RelativeLayout>

* layout_align... - выравнивание элемента относительно указанного

    * layout_alignBottom - снизу
    * layout_alignLeft - слева
    * layout_alignRight - справа
    * layout_alignTop - сверху

* layout_alignParent... - выравнивание элемента относительно родителя

    * layout_alignParentBottom -  снизу
    * layout_alignParentLeft - слева
    * layout_alignParentRight - справа
    * layout_alignParentTop - сверху

* layout_center... - выравниваение элемента по центру относительно родителя

    * layout_centerVertical - вертикально
    * layout_centerHorizontal - горизонтально
    * layout_centerInParent - по центру вертикально и горизонтально относительно родителя

* layout_height - высота элемента

    * match_parent - заполнить родителя
    * wrap_content - по содержимому

* layout_to... - расположить элемент относительно указанного

    * layout_above - сверху
    * layout_below - снизу
    * layout_toLeftOf - слева
    * layout_toRightOf - справа

* layout_width - ширина элемента

    * match_parent - заполнить родителя
    * wrap_content - по содержимому


.. py:class:: RelativeLayout()

    Наследник :py:class:`android.view.ViewGroup`

    .. py:class:: LayoutParams()

        Настройки слоя

        Наследник :py:class:`android.view.ViewGroup.LayoutParams`
