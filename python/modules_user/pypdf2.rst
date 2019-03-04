.. py:module:: pypdf2

pypdf2
======

.. code-block:: sh

    pip install pypdf2


PdfFileReader()
---------------

.. py:class:: PdfFileReader(file_obj)

    .. code-block:: py

        pdf = PdfFileReader(open('ilnurgi.pdf'))

    
    .. py:method:: getDocumentInfo()

        Возвращает :py:class:`DocumentInformation`

        .. code-block:: py

            pdf.getDocumentInfo()

    
    .. py:method:: getNumPages()

        Возвращает количесвто траниц в документе

        .. code-block:: py

            pdf.getNumPages()
            # 3

    .. py:method:: getPage(page_number)

        .. code-block:: py

            pdf.getPage(1)


PdfFileWriter()
---------------

.. py:class:: PdfFileWriter()

    .. code-block:: py

        pdf_writer = PdfFileWriter()


    .. py:method:: addPage()

        Добавляет страницу в документ

        .. code-block:: py

            pdf_writer.addPage(pdf.getPage(1))


    .. py:method:: write(file_object)

        Записывает pdf документ в файл

        .. code-block:: py

            pdf_writer.write(open('new_pdf.pdf'))


PdfFileMerger()
---------------

.. py:class:: PdfFileMerger()

    .. code-block:: py

        file_merger = PdfFileMerger()

        for path in paths:
            file_merger.append(path)

        file_merger.write(open('merged_pdf.pdf'))


DocumentInformation()
---------------------

.. py:class:: DocumentInformation()

    .. py:attribute:: author

    .. py:attribute:: creator

    .. py:attribute:: producer

    .. py:attribute:: subject

    .. py:attribute:: title
