.. title:: android.widget.TextView

.. meta::
    :description:
        Справочная информация по android классу android.widget.TextView.
    :keywords:
        android widget TextView

.. py:currentmodule:: android.widget

TextView()
==========

.. code-block:: xml

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"

        android:gravity="center_horizontal"
        android:text="some_text"
        android:id="@+id/textView1" />

clickable
---------


id
--

Идентификатор элемента

.. code-block:: xml

    <TextView android:id="@+id/textView" />


gravity
-------

Положение содержимого внутри элемента

.. code-block:: xml

    <TextView android:gravity="center" />
    <TextView android:gravity="center_horizontal" />
    <TextView android:layout_gravity="top|bottom|left|right|center" />
    

layout_height
-------------

Высота элемента

.. code-block:: xml
    
    <!-- заполнить родителя -->
    <TextView android:layout_height="match_parent" />

    <!-- по содержимому -->
    <TextView android:layout_height="wrap_content" />

    <TextView android:layout_height="200dp" />


layout_width
------------

Ширина элемента

.. code-block:: xml

    <!-- заполнить родителя -->
    <TextView android:layout_width="match_parent" />

    <!-- по содержимому -->
    <TextView android:layout_width="wrap_content" />
    
    <TextView android:layout_width="200dp" />


minHeight
---------


onClick
-------

Обработчик клика


text
----

Текст внутри элемента

.. code-block:: xml

    <TextView android:text="text" />
    <TextView android:text="@string/tv" />


textSize
--------

Hазмер шрифта текст

.. code-block:: xml

    <TextView android:textSize="8pt"/>
    <TextView android:textSize="8dp"/>
    <TextView android:textSize="8sp"/>


TextView()
----------

.. py:class:: TextView([context[, attrs, [defStyle]]])

    Поддерживает многострочное отображение,
    форматирование и автоматический перенос слов и символов.

    Наследник :py:class:`android.view.View`

    * context - :py:class:`android.content.Context`

    * attrs - :py:class:`android.util.AttributeSet`

    * defStyle - int

    .. code-block:: java

        TextView textView = (TextView)findViewById(R.id.textView);


    .. py:method:: getText()

        Возвращает текст виджета


    .. py:method:: onDraw(Canvas canvas)

        * canvas - :py:class:`android.graphics.Canvas`


    .. py:method:: onKeyDown(int keyCode, KeyEvent keyEvent)


    .. py:method:: setGravity(gravity)

        Устанавливает выравнивание текста внутри элемента

        .. code-block:: java

            textView.setGravity(gravity)


    .. py:method:: setLayoutParams(layoutParams)

        Задает параметры для вьюхи

        .. code-block:: java

            textView.setLayoutParams(
                new LayoutParams(
                    LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT));


    .. py:method:: setText(String text)
    .. py:method:: setText(int id)

        Устанавливает текст виджета

        .. code-block:: java

            textView.setText(textView.getText());
            textView.setText(R.string.name);
            textView.setText("Some text");


    .. py:method:: setTextSize(size)

        устанавливает размер текст для объекта


    .. py:method:: setTextColor(color)

        устанавливает цвет текст для объекта

        .. code-block:: java

            textView.setTextColor("red");


    .. py:method:: startAnimation(Animation anim)

        Запускается анимацию элемента

        * anim - :py:class:`android.view.animation.Animation`

        .. code-block:: java

            textView.startAnimation(anim);


    .. py:method:: requestFocus()

        устанавливает фокус на виджет
