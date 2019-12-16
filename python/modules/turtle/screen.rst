.. title:: python turtle Screen

.. meta::
    :description:
        Справочная информация по python модулю turtle.
        Модуль для разработки графической части приложения, холст для рисования.
        Screen - окно рисования.
    :keywords:
        python turtle Screen

.. py:currentmodule:: turtle


Screen()
========

.. py:class:: Screen()

    Окно рисования

    .. code-block:: py

        screen = Screen()

        screen.done()
        screen.close()

    .. py:method:: bgpic(shape_name)

        Устанавливает фон для окна

        .. code-block:: py

            turtle.register_shape('bg.gif')
            screen.bgpic('bg.gif')


    .. py:method:: close()

        Закрывате и завершает программу корректно

        .. code-block:: py

            screen.close()

    .. py:method:: done()

        Открывает окно программы и запускает бесконечный цикл обработки событий

        .. code-block:: py

            screen.done()


    .. py:method:: listen()

        .. code-block:: py

            screen.listen()

    .. py:method:: onkey(callback_fn, key)

        Вешаем обработчик события кнопки

        .. code-block:: py

            screen.onkey(callback_fn, 'd')
