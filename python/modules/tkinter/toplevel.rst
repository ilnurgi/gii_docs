TopLevel - виджет, окно верхнего уровня
=======================================


.. py:class:: TopLevel(**kwargs)

    Окно верхнего уровня

    Наследник :py:class:`BaseWidget`, :py:class:`WM`

    .. code-block:: py

        # модальное окно
        modal_window = TopLevel(root)
        Button(modal_window, command=lambda: modal_window.destroy())

        modal_window.focus_set()
        modal_window.grab_set()
        modal_window.wait_window()

        modal_window.mainloop()


    .. py:method:: focus_set()

        Захватывает фокус

        .. code-block:: py

            modal_window.focus_set()


    .. py:method:: grab_set()

        Забрать себе фокус

        .. code-block:: py

            modal_window.grab_set()


    .. py:method:: wait_window()

        .. code-block::py

            modal_window.wait_window()
