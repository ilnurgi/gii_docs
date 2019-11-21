.. title:: android.widget.TableLayout

.. meta::
    :description:
        Справочная информация по android классу android.widget.TableLayout.
    :keywords:
        android widget TableLayout

.. py:currentmodule:: android.widget

TableLayout()
=============

Контейнер, распологает элементы с помощью сетки, таблицы, состоящей из строк и столбцов.

При этом столбцы могут либо автоматически растягиваться, либо оставаться постоянной ширины.

.. code-block:: xml

    <TableLayout

        android:layout_height="wrap_content"
        android:layout_width="match_parent"

        android:id="@+id/tableLayout1">

        <TableRow
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"

            android:id="@+id/tableRow1">

            <Button
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"

                android:text="Button"
                android:id="@+id/button3" />

        </TableRow>

    </TableLayout>

* id - идентификатор элемента

    * @+id/identifier

* stretchColumns

* layout_height - высота элемента

    * match_parent - заполнить родителя
    * wrap_content - по содержимому
    * 10dp

* layout_width - ширина элемента

    * match_parent - заполнить родителя
    * wrap_content - по содержимому
    * 20 dp

.. py:class:: TableLayout()

    .. py:class:: LayoutParams()

        Настройки слоя

        Наследник :py:class:`android.view.ViewGroup.LayoutParams`

