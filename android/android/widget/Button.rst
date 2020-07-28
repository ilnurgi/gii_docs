.. title:: android.widget.Button

.. meta::
    :description:
        Справочная информация по android классу android.widget.Button.
    :keywords:
        android widget Button

.. py:currentmodule:: android.widget

Button()
========

.. code-block:: xml

    <Button />


gravity
-------

Положение содержимого внутри элемента

.. code-block:: xml

    <Button android:gravity="center" />
    <Button android:gravity="center_horizontal" />


id
--

Идентификатор элемента

.. code-block:: xml

    <Button android:id="@+id/button" />


layout_gravity
--------------

Положение элемента внутри родителя

.. code-block:: xml
    
    <Button android:layout_gravity="top|left" />
    <Button android:layout_gravity="top|bottom|left|right|center" />
    <Button android:gravity="center_horizontal" />


layout_height
-------------

Высота элемента

.. code-block:: xml
    
    <!-- заполнить родителя -->
    <Button android:layout_height="match_parent" />

    <!-- по содержимому -->
    <Button android:layout_height="wrap_content" />

    <Button android:layout_height="200dp" />


layout_width
------------

Ширина элемента

.. code-block:: xml

    <!-- заполнить родителя -->
    <Button android:layout_width="match_parent" />

    <!-- по содержимому -->
    <Button android:layout_width="wrap_content" />

    <Button android:layout_width="200dp" />


onClick
-------

Название метода активити, который обработает клик по элементу.

Метод принимает один аргумент c типом :py:class:`android.view.View` и должен быть public void.


text
----

Текст внутри элемента

.. code-block:: xml

    <Button android:text="button text" />
    <Button android:text="@string/btn2" />


textSize
--------

Hазмер шрифта текст

.. code-block:: xml

    <Button android:textSize="8pt"/>
    <Button android:textSize="8dp"/>
    <Button android:textSize="8sp"/>


Button()
--------

.. py:class:: Button()

    Наследник :py:class:`android.widget.TextView`

    .. code-block:: java

        Button myBtn = (Button) findViewById(R.id.myBtn);


    .. py:method:: getLayoutParams()

        Возвращает параметры кнопки :py:class:`android.view.ViewGroup.LayoutParams`

        .. code-block:: java

            LayoutParams lparams = (LayoutParams) myBtn.getLayoutParams()


    .. py:method:: requestLayout()

        Перерисовывает элемент

        .. code-block:: java

            myBtn.requestLayout()


    .. py:method:: setText(str)
    .. py:method:: setText(R.string.name)

        устанавливает текст для объекта

        .. code-block:: java

            myBtn.setText("Some text");
            myBtn.setText(R.string.btnText);


    .. py:method:: setEnabled(bool)

        активность кнопки

        .. code-block:: java

            myBtn.setEnabled(false);


    .. py:method:: setOnClickListener(OnClickListener)

        Устанавливает обработчик клика по элементу

        * **OnClickListener** - :py:class:`android.view.View.OnClickListener`

        .. code-block:: java

            myBtn.setOnClickListener(new OnClickListener(){

                @Override
                public void onClick(View v){}

            });
