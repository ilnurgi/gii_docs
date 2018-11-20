.. py:module:: beautifulsoup

beautifulsoup
=============

https://www.crummy.com/software/BeautifulSoup/bs4/doc/

.. code-block:: shell

    pip install beautifulsoup4

.. code-block:: py
    
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html_text)
    links = [element.get('href') for element in soup.find_all('a')]


BeautifulSoup()
---------------

.. py:class:: BeautifulSoup(html_text: str, parser: str = 'html.parser')

    Парсер html

    .. code-block:: py

        soup = BeautifulSoup(some_html_string)
        soup = BeautifulSoup(some_html_string, 'html.parser')
        soup = BeautifulSoup(some_html_string, 'lxml')
        soup = BeautifulSoup(some_html_string, 'lxml-xml')
        soup = BeautifulSoup(some_html_string, 'html5lib')


    .. py:attribute:: body -> :py:class:`beautifulsoup.element.Tag`

    .. py:attribute:: head -> :py:class:`beautifulsoup.element.Tag`

    .. py:attribute:: title -> :py:class:`beautifulsoup.element.Tag`

    .. py:method:: get_test() -> str

        Возвращает строку, весь текст, без html страницы


    .. py:method:: find(name=None, attributes={}, recursive=True, text=None, *kwargs)

        Возвращает первый найденный элемент


    .. py:method:: findAll(name=None, attributes={}, recursive=True, text=None, limit=None, *kwargs) -> :py:class:`beautifulsoup.element.ResultSet`

        Поиск элементов на странице

        .. code-block:: py

            span_list = bs_obj.findAll('span', {'class': 'green'})
            for span in span_list:
                print(span.get_text())

            hs = bs_obj.findAll({'h1', 'h2', 'h3', 'h4', 'h5', 'h6'})

            id_text_elem = bs_obj.findAll(id='text')

            imgs = bs_obj.findAll('img', {'src': re.compile('\.\.\/img\/*\.jpg')})

            imgs = bs_obj.findAll(lambda tag: len(tag.attrs) == 2)


    .. py:method:: prettify() -> str

        Возвращает строку, отформатированныую строку содержимого 

        .. code-block:: py

            print(soup.prettify())






Comment()
---------

.. py:class:: Comment()

    Коментарии