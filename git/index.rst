.. title:: git

.. meta::
    :description:
        Справочная информация по системе контроля версии, git.
    :keywords:
        git

Git
===

.. code-block:: sh

    $ git help
    $ git help commit


Конфигурирование
----------------

.. code-block:: sh

    $ git config --global user.name "UserName"

    $ git config --global user.email "email@email.ru"

    $ git config --list
    user.name=UserName
    user.email=email@email.ru

    $ cat ~/.gitconfig
    [user]
        name = UserName
        email = email@email.ru


Инициализация
-------------

.. code-block:: sh

    $ git init


Состояние
---------

.. code-block:: sh

    $ git status


Индекс
------

.. code-block:: sh

    # добавление измененй в индекс
    $ git add .
    $ git add index.html

    # просмотр изменений
    $ git diff
    $ git diff --staged

    # вернуть файл в исходное состояние
    $ git checkout index.html

    # вернуть файл в состояние, как в указанном комите
    $ git checkout commit_hash index.html

    # удалить изменения из индекса
    $ git reset HEAD index.html

    # удалить файл из репы
    $ git rm index2.html
    # без физического удаления файла с диска
    $ git rm --cached index2.html


Комит
-----

.. code-block:: sh

    $ git commit -m "commit message"
    $ git commit --amend -m "new commit message"
    $ git commit --amend --no-edit

    $ git log
    $ git log -1
    $ git log --oneline
    $ git log --oneline --all
    $ git log --oneline --all --graph

    $ git show commit_hash

    $ git cat-file -p commit_hash


Ветки
-----

.. code-block:: sh

    $ git checkout commit_hash
    $ git checkout -b new_branch

    $ git merge new_branch -m "merge commit"
