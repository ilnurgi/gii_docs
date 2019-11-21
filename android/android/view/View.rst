.. title:: android.view.View

.. meta::
    :description:
        Справочная информация по android классу android.view.View().
    :keywords:
        android view View

.. py:currentmodule:: android.view

View()
======

.. py:class:: View()

    Базовый класс для всех компонентов интерфейса

    Наследник :py:class:`java.lang.Object`


    .. py:method:: getId()

        возвращает id объекта


    .. py:method:: setBackgroundResource(R.color.name)

        устанавливает фоновый цвет


    .. py:method:: setOnCreateContextMenuListener(obj)

        утсанавливает обработчик контекстного меню, obj например this - Activity


    .. py:method:: onMeasure(width, height)

        задает размер области для вью

        :param width: int
        :param height: int
        :rtype: void


    .. py:method:: setMeasuredDimension(measuredHeight, measuredWidth);

        устанавливает размер области

        :param measuredHeight: int
        :param measuredWidth: int


    .. py:method:: setOnClickListener(OnClickListener)

        Устанавливает обработчик клика по элементу

        * OnClickListener - :py:class:`android.view.View.OnClickListener`

        .. code-block:: java

            someView.setOnClickListener(new OnClickListener(){

                @Override
                public void onClick(View v){
                    ...
                }

            });

    .. py:class:: OnClickListener()

        Интерфейс, обработчик нажатий элемента


        .. py:method:: onClick(view)

            Обработчик элемента

            * view - :py:class:`android.view.View`

            .. code-block:: java

                OnClickListener oclBtnOk = new OnClickListener() {

                    @Override
                    publick void onClick(View v){};
                };


    .. py:class:: MeasureSpec()


        .. py:attribute:: UNSPECIFIED


        .. py:method:: getMode(?)


        .. py:method:: getSize(?)
