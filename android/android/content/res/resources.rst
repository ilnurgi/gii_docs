.. title:: android.content.res.Resources

.. meta::
    :description:
        Справочная информация по android, класс android.content.res.Resources.
    :keywords:
        android.content.res.Resources

.. py:currentmodule:: android.content.res

Resources()
===========


.. py:class:: Resources()

    Таблица ресурсов приложения

    .. code-block:: java

        Resources resource = activity.getResources()


    .. py:method:: getColor(R.color.id)

        Возвращает ресурс цвет по идентификатору


    .. py:method:: getDimension(R.dim.id)

        Возвращает ресурс размер по идентификатору


    .. py:method:: getDrawable(R.drawable.id)

        Возвращает ресурс изображение по идентификатору


    .. py:method:: getQuantityString(id, quantity)

        * **id** - Int - идентификатор ресурса
        * **quantity** - Int

        Возвращает String, значение ресурса для множественного числа

        .. code-block:: xml

            <plurals name="minutes">
                <item quantity="one">minute</item>
                <item quantity="other">minutes</item>
            </plurals>

        .. code-block:: java

            int minutes = Calendar.getInstance().get(Calendar.MINUTE);
            getQuantityString(R.plurals.minutes, minutes);


    .. py:method:: getQuantityString(id, quantity, foramtArgs)


    .. py:method:: getString(id)

        * **id** - Int - идентификатор ресурса

        Возвращает String, значение ресурса

        .. code-block:: xml

            <string name="login_welcome">Привет</string>

        .. code-block:: java

            getString(R.string.login_welcome)
            // Привет


    .. py:method:: getString(id, formatArgs)

        * **id** - Int - идентификатор ресурса
        * ***formatArgs* - Any - форматирование строки

        Возвращает String, отформатированное значение ресурса

        .. code-block:: xml

            <string name="login_welcome">Привет, %s</string>

        .. code-block:: java

            getString(R.string.login_welcome, "ilnurgi")
            // Привет, ilnurgi



    .. py:method:: getStringArray(int arrayId)

        Возвращает Array<String>, ресурс массив по идентификатору

        .. code-block:: java

            String[] names = resource.getStringArray(R.array.names);


    .. py:method:: getText(id)

        возвращает текст по идентификатору

        .. code-block:: java

            CharSequence styledText = myResources.getText(R.string.stop_message);


Resources.NotFoundException
---------------------------

.. py:class:: android.content.res.Resources.NotFoundException()

