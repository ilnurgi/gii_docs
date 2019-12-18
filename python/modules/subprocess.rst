.. title:: python subprocess

.. meta::
    :description:
        Справочная информация по python модулю subprocess.
    :keywords:
        python subprocess

.. py:module:: subprocess

subprocess
==========

DEVNULL
-------

.. py:attribute:: DEVNULL


PIPE
----

.. py:attribute:: PIPE


run()
-----

.. py:method:: run(command_list, **kwargs)

    * **check** - булево, рейзить ошибку, если код возврата команды не 0
    * **input**
    * **stderr** - входной поток данных
    * **stdin** - выходной поток данных по ошибкам
    * **stdout** - выходной поток данных
    * **text** - булево, stdout, stdin вернут строки, а не байты

    .. code-block:: py

        list_files = subprocess.run(['ls', '-l'])
        list_files.returncode
        # 0

        subprocess.run(['ls', '-l', '-a', '-h'])
        subprocess.run(['ls', '-l'], stdout=subprocess.DEVNULL)

        cat = subprocess.run(['cat'], stdout=subprocess.PIPE, text=True, input='ilnurgi')
        cat.stdout
        # ilnurgi

        subprocess.run(['bad_command'], check=True)
        # Error


Popen()
-------

.. py:class:: Popen(command_list, **kwargs)

    * **stderr** - входной поток данных
    * **stdin** - выходной поток данных по ошибкам
    * **stdout** - выходной поток данных
    * **text** - булево, stdout, stdin вернут строки, а не байты

    .. code-block:: py

        ls_cmd = Popen(['ls', '-l']
        cat_cmd = Popen(
            ['cat'], 
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )


    .. py:method:: communicate(**kwargs)

        * **input**

        .. code-block:: py

            output, errors = cat_cmd.communicate(input='ilnurgi')


    .. py:method:: poll()

        .. code-block:: py

            cat_cmd.poll()


    .. py:method:: wait()

        .. code-block:: py

            cat_cmd.wait()

