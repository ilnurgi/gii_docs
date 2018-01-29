path
====

.. code-block:: js

    consta path = require('path');


basename
--------

.. js:function:: basename()

    Возвращает имя файла без расширения

    .. code-block:: js

        file_name = path.basename('index.html');


extname
-------

.. js:function:: extname()

    Возвращает расширение файла

    .. code-block:: js

        ext = path.extname('index.html');


join
----

.. js:function:: join()

    Создает валидный путь из аргументов для конкретной операционной системы

    .. code-block:: js

        const static_path = path.join(__dirname, 'static')