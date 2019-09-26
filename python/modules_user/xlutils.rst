.. title:: xlutils

.. meta::
    :description: xlutils
    :keywords: xlutils

.. py:module:: xlutils

xlutils
=======

http://pythonhosted.org/xlutils/

Модуль с утилитами, для работы с Excel файлами

copy()
------

.. py:method:: copy()
    
    Копируют объект :py:class:`xlrd.Book` в объект :py:class:`xlwt.Workbook`

    .. note:: Рекомендуется использовать pass on_demand=True в open_workbook() это экономит память

    .. code-block:: py

        import os

        from xlrd import open_workbook

        from xlutils.copy import copy
        
        rb = open_workbook('testall.xls', formatting_info=True, on_demand=True)

        rb.sheet_by_index(0).cell(0, 0).value
        # 'R0C0'
        
        #rb.sheet_by_index(0).cell(0, 1).value
        'R0C1'

        wb = copy(rb)

        wb.get_sheet(0).write(0, 0, 'changed!')
        wb.save('output.xls')
        temp_dir.listdir()
        # ['output.xls']

        rb = open_workbook('output.xls')
        
        rb.sheet_by_index(0).cell(0, 0).value
        # 'changed!'
        
        # rb.sheet_by_index(0).cell(0, 1).value
        # 'R0C1'


quoted_sheet_name()
-------------------

.. py:method:: quoted_sheet_name(sheet_name, encoding='ascii')
    
    Возвращает строку, название листа.

    .. code-block:: py

        from xlutils.display import quoted_sheet_name
        
        quoted_sheet_name('Price(\xa3)', 'utf-8')
        # 'Price(\xc2\xa3)'

        quoted_sheet_name('My Sheet')
        # "'My Sheet'"

        quoted_sheet_name(u"John's Sheet")
        # "'John''s Sheet'"


cell_display()
--------------

.. py:method:: cell_display(cell, datemode=0, encoding='ascii')
    
    Возвращает строковое представление ячейки

    .. code-block:: py

        import xlrd
        from xlrd.sheet import Cell
        
        from xlutils.display import cell_display

        cell_display(Cell(xlrd.XL_CELL_EMPTY, ''))
        # 'undefined'

        cell_display(Cell(xlrd.XL_CELL_BLANK, ''))
        # 'blank'

        cell_display(Cell(xlrd.XL_CELL_NUMBER, 1.2))
        # 'number (1.2000)'

        cell_display(Cell(xlrd.XL_CELL_BOOLEAN, 0))
        # 'logical (FALSE)'

        cell_display(Cell(xlrd.XL_CELL_DATE, 36892.0))
        # 'date (2001-01-01 00:00:00)'

        cell_display(Cell(xlrd.XL_CELL_DATE, 1.5))
        # 'date? (1.500000)'

        wb = open_workbook('date.xls')
        
        cell = wb.sheet_by_index(0).cell(0, 0)
        cell_display(cell, wb.datemode)
        # 'date (2012-04-13 00:00:00)'

        cell_display(Cell(xlrd.XL_CELL_TEXT,u'Price (\xa3)'))
        # 'text (Price (?))'

        cell_display(Cell(xlrd.XL_CELL_TEXT,u'Price (\xa3)'), encoding='utf-8')
        # 'text (Price (\xc2\xa3))'

        cell_display(Cell(xlrd.XL_CELL_ERROR, 0))
        # 'error (#NULL!)'

        cell_display(Cell(xlrd.XL_CELL_ERROR, 2000))
        # 'unknown error code (2000)'

        cell_display(Cell(69, 0))
        """
        Traceback (most recent call last):
        ...
        Exception: Unknown Cell.ctype: 69
        """
