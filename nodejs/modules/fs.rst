fs
==

Модуль для работы с файлами

.. code-block:: js

    const fs = require('fs');


appendFile
----------

.. js:function:: appendFile()

    Дописывает данные в файл

    .. code-block:: js

        fs.appendFile('hello.txt', 'appended content', function(err){
            // ...
        });

lstat
-----

.. js:function:: lstat(file, (err, stat) => {})

    

mkdir, mkdirSync
----------------

.. js:function:: mkdir()

    Создает папку по указанному пути

    .. code-block:: js

        js.mkdir('myFolder');


readdir, readdirSync
--------------------

.. js:function:: readdir()
.. js:function:: readdirSync()

    Чтение содержимого папки

    .. code-block:: js

        fs.readdir('myFolder', function(err, file){
            files.forEach(function(file){
                // ...
            });
        });


readFile, readFileSync
----------------------

.. js:function:: readFileSync(file_path, params)

    Возвращает строку, содержимое файла

    .. code-block:: js

        let content = fs.readFileSync('./index.html');
        let content = fs.readFileSync(__dirname + '/index.html', {
            encoding: 'utf-8'
        }); 

    .. code-block:: js

        let buffer = fs.readFileSync('./index.html', 'utf-8');
        const src = buffer.toString();

    .. code-block:: js

        fs.readFile('./1.txt', 'utf-8', (err, buffer) => {
            // ...
        });


renameSync
----------

.. js:function:: renameSync()

    Переименовать файл

    .. code-block:: js

        fs.renameSync('src.txt', 'dst.txt');


writeFile, writeFileSync
------------------------

.. js:function:: writeFile()

    Записывает данные в файл

    .. code-block:: js

        fs.writeFile('hello.txt', 'content', function(err){
            // ...
        });