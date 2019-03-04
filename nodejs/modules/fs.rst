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


readFile(), readFileSync()
--------------------------

.. js:function:: readFile(file_path)
.. js:function:: readFileSync(file_path)

    Возвращает строку, содержимое файла

    .. code-block:: js

        let content = fs.readFileSync('./index.html');
        let content = fs.readFileSync(__dirname + '/index.html', {
            encoding: 'utf-8'
        });


renameSync
----------

.. js:function:: renameSync()

    Переименовать файл

    .. code-block:: js

        fs.renameSync('src.txt', 'dst.txt');


statSync()
----------

.. js:function:: statSync()

    .. code-block:: js

        const stats = fs.statSync(filename);
        console.log(stats.mtime.valueOf())


watch()
-------

.. js:function:: watch(path)

    Следит за файлом или за файлами в папке через системные уведомления

    .. code-block:: js

        fs.watch('./', (event, filename) => {
            if (filename and event === 'change') {
                // file changed
            }
        });



watchFile()
-----------

.. js:function:: watchFile(path, options, callback)

    Следит за файлом и вызывает колбек при изменении файла

    * options 
        * interval - задает время опроса файла на изменение, по умолчанию 5 секунд

    .. code-block:: js

        fs.watchFile('./some.js', (curr, prev) => {
            // ...
            // prev.mtime - время предыдущей модификации файла
        });

        fs.watchFile('./some.js', {interval: 1000}, (curr, prev) => {
            // ...
            // prev.mtime - время предыдущей модификации файла
        });


writeFile
---------

.. js:function:: writeFile()

    Записывает данные в файл

    .. code-block:: js

        fs.writeFile('hello.txt', 'content', function(err){
            // ...
        });