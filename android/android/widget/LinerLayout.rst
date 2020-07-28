.. title:: android.widget.LinearLayout

.. meta::
    :description:
        Справочная информация по android классу android.widget.LinearLayout.
    :keywords:
        android widget LinearLayout

.. py:currentmodule:: android.widget

LinerLayout()
=============

Контейнер, который распологает элементы внутри себя в линию по горизонтали или по вертикали.

.. code-block:: xml

    <LinerLayout
        xmlns:android="http://schemas.android.com/apk/res/android"

        android:layout_width="wrap_content"
        android:layout_height="wrap_content"

        android:orientation="vertical"
        android:id="@+id/layout"/>

background
----------

Фон


id
--

Идентификатор элемента

.. code-block:: xml

    <LinerLayout android:id="@+id/liner_layout" />


orientation
-------------

Порядок заполнения виджетами контейнера

.. code-block:: xml

    <LinerLayout android:orientation="vertical" />
    <LinerLayout android:orientation="horizontal" />


layout_gravity
--------------

Выравнивание элемента в родителе

.. code-block:: xml
    
    <LinerLayout android:layout_gravity="top|left" />
    <LinerLayout android:layout_gravity="top|bottom|left|right|center" />
    <LinerLayout android:gravity="center_horizontal" />


layout_height
-------------

Высота элемента

.. code-block:: xml
    
    <!-- заполнить родителя -->
    <LinerLayout android:layout_height="match_parent" />

    <!-- по содержимому -->
    <LinerLayout android:layout_height="wrap_content" />

    <LinerLayout android:layout_height="200dp" />


layout_margin
-------------

Внешние отступы элемента

.. code-block:: xml

    <LayoutParams android:layout_margin="layout_marginLeft" />
    <LayoutParams android:layout_margin="layout_marginRight" />
    <LayoutParams android:layout_margin="layout_marginBottom" />
    <LayoutParams android:layout_margin="layout_marginTop" />


layout_width
------------

Ширина элемента

.. code-block:: xml

    <!-- заполнить родителя -->
    <LinerLayout android:layout_width="match_parent" />

    <!-- по содержимому -->
    <LinerLayout android:layout_width="wrap_content" />

    <LinerLayout android:layout_width="200dp" />


layout_weight
-------------

Вес элемента, для заполнения родителя


LinerLayout()
-------------

.. py:class:: LinerLayout()

    Наследник :py:class:`android.view.ViewGroup`


    .. py:attribute:: VERTICAL

        Статическая константа, вертикальный лейаут


    .. py:method:: addView(View view)

        Добавляет вью в слой

        .. code-block:: java

            linearLayout.addView(someView);
            linearLayout.addView(someView, viewLayoutParams);


    .. py:method:: removeAllViews()

        Удаляет все элементы со слоя

        .. code-block:: java

            linearLayout.removeAllViews()


    .. py:method:: setOrientation(orientation)

        Устанавливает ориентацию для слоя

        * LinearLayout.VERTICAL
        * LinearLayout.HORIZONTAL

        .. code-block:: java

            linearLayout.setOrientation(LinearLayout.VERTICAL);

    .. py:class:: LayoutParams()

        Настройки слоя

        Наследник :py:class:`android.view.ViewGroup.MarginLayoutParams`

        .. code-block:: java

            LinerLayout.LayoutParams linearLayout = new LinerLayout.LayoutParams(
                ViewGroup.LayoutParams.WRAP_CONTENT,
                ViewGroup.LayoutParams.WRAP_CONTENT);
            linearLayout.leftMargin = 50;

        .. py:attribute:: gravity
        .. py:attribute:: weight
