.. py:module:: openpyxl

openpyxl
========

.. code-block:: py

    from openpyxl import load_workbook
 
    workbook = load_workbook('/path/to/file.xlsx')
     
    # get all worksheets
    all_sheets = workbook.get_sheet_names()
     
    first_sheet = all_sheets[0]
     
    # get a worksheet by its name
    worksheet = workbook.get_sheet_by_name(first_sheet)
     
    # print all rows in a worksheet
    for row in worksheet.iter_rows():
        print(row)
     
        # all the values in a row
        for cell in row:
            print(cell)
            # get cell value
            print(cell.value)
    # get cell with row number and column number
    worksheet.cell(row=1, column=2).value

.. code-block:: py

    from openpyxl import Workbook
 
    workbook = Workbook()
     
    # create xls workbook sheet
    workbook.create_sheet(index=0, title='Sheet1')
    workbook.create_sheet(index=0, title='Sheet2')
     
    # remove xls workbook sheet
    workbook.remove(workbook['Sheet2'])
     
    # get active work sheet
    work_sheet = workbook.active
     
    data = [
        ['Naveen', 'M', 'Software Engineer'],
        ['David', 'N', 'Designer'],
        ['Shera', 'H', 'Web Developer']
    ]
     
    rows = 3
    cols = 3
    # iterate to set data
    for row_num in range(0, rows):
        for col_num in range (0, cols):
            work_sheet.cell(
                row=row_num + 1,
                column=col_num + 1
            ).value = data[row_num][col_num]
     
    # save data to xls file
    workbook.save('output.xlsx')