.. title:: python argparse

.. meta::
    :description: 
        Справочная информация по базовому модулю python, argparse.
        argparse предназначен для работы с аргументами коммандной строки.

    :keywords:
        python argparse

.. py:module:: argparse

argparse
========

.. code-block:: py

    import argparse

    import os
    import sys

    arg_parser = argparse.ArgumentParser(description='arg parser description')

    my_parser.add_argument(
        'Path',
        metavar='path',
        type=str,
        help='the path',
    )

    my_parser.parse_args(['/home/ilnurgi/'])
    # Namespace(Path='/home/ilnurgi/')

    my_parser.parse_args([])
    # usage: script.py [-h] path
    # script.py: error: the following arguments are required: path

    my_parser.parse_args([-h])
    """
    usage: script.py [-h] path

    arg parser description

    positional arguments:
    path        the path

    optional arguments:
    -h, --help  show this help message and exit
    """


Action()
--------

.. py:class:: Action(option_strings, dest, nargs=None, const=None, default=None, type=None, choises=None, required=None, help=None, metavar=None)

    Действие для аргумента

    .. code-block:: py

        class MyAction(Action):

            def __init__(self, option_strings, dest, nargs, **kwargs):
                """"""

            def __call__(self, parser, namespace, values, option_string=None):
                """"""

        arg_parser.add_argument('-i', '--input', action=MyAction, type=int)



ArgumentParser()
----------------

.. py:class:: ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error',  add_help=True, allow_abbrev=True)

    * prog - название программы, которое будет отображаться в консоли. По умолчанию будет название скрипта

    * usage - текст примера использования

    * description - описание программы, которое будет выводиться в консоли

    * epilog - текст, который будет выведен в консоли после всей информации

    * parents - список :py:class:`argparse.ArgumentParser()` ключи которой будут включены в текущий объект

    * formatter_class - объект, форматирующий вывод сообщения помощи. 

        * :py:class:`argparse.HelpFormatter()`
        * :py:class:`argparse.RawDescriptionHelpFormatter()`
        * :py:class:`argparse.RawTextHelpFormatter()`
        * :py:class:`argparse.ArgumentDefaultsHelpFormatter()`
        * :py:class:`argparse.MetavarTypeHelpFormatter()`

    * prefix_chars - префикс для параметрв

    * fromfile_prefix_chars - префикс для параметра, который указывает на файл с параметрами. Если параметров много, то можно их передать через файл.

    * allow_abbrev - учитывать абреавитуры Например если есть аргумент --input, то с консоли его можно перадать и как --input, и как --inpu, --inp, --in. 

    * add_help - добавить автоматический параметр -h, хелпер.

    .. code-block:: py

        arg_parser = ArgumentParser(
            prog='myprog', 
            description='argparse description',
            usage='%(prog)s [options] path',
            epilog='from ilnurgi',
            prefix='/',
            fromfile_prefix_chars='@',
        )

        arg_parser.parse_args(['@params.txt'])
        # Namespace()

    .. py:method:: add_argument(...values, action='store', nargs, const, default, type, choises, required, help, metavar, dest)

        Добавляет параметр в парсер

        * values - параметры для парсинга, если указан без префикса, то параметр считается как позиционный

        * action - что делать с параметром

            * store - сохранить в сам объект
            * store_const - если параметр указан, то взять константу из парсера
            * store_true - если параметр указан, то значение будет False
            * store_false - если параметр указан, то значение будет True
            * append - может быть указано несколько раз, все праметры будут собраны в список
            * append_const - может быть указано несколько раз, константный значение парсера собрать в список
            * count - сколько раз параметр был указан
            * help - показать хелп и выйти
            * version - показать версию программы и выйти
            * :py:class:`argparse.Action()` - свой обработчик

        * nargs - указывает количесвто параметров, которое должно быть передано

            * число - конкретное значение
            * ? - одно значение
            * \* - 0 или несколько
            * + - 1 или несколько
            * argparse.REMAINDER - оставшиеся аргументы

        * const - значение по умолчанию, либо callable объект, который вернет значение

        * default - значение по умолчанию, либо callable объект, который вернет значение
        
        * type - тип значения

        * choises - перечисление возможных значений
        
        * required - булево, поле обязательно

        * help - текст помощи

        * metavar - доп информация по атрибуту, например для поля с датой формат даты можно указать

        * dest - название переменной, куда поместим параметр


        .. code-block:: py

            # позиционный аргумент Path, обязательный
            arg_parser.add_argument(
                'Path',
                metavar='path',
                type=str,
                help='the path',
            )

            # позиционный необязательный аргумент
            arg_parser.add_argument(
                'Path',
                metavar='path',
                type=str,
                help='the path',
                # за счет этого параметр не обязательный
                nargs='?'
            )

            # опциональный аргумент -v, --verbose
            arg_parser.add_argument(
                '-v', 
                '--verbose',
                action='store_true',
                help='optional argument',
            )

            arg_parser.parse_args(['/home/ilnurgi/'])
            # Namespace(Path='/home/ilnurgi/')

        .. code-block:: py

            arg_parser.add_argument(
                '--input', 
                action='store',
                type='int',
                required=True,
            )

            arg_parser.parse_args(['--input', 42])
            # Namespace(input=42)

            arg_parser.parse_args(['--inpu', 42])
            # Namespace(input=42)

            arg_parser.parse_args(['--inp', 42])
            # Namespace(input=42)

            arg_parser.parse_args(['--in', 42])
            # Namespace(input=42)

        .. code-block:: py

            arg_parser.add_argument('-b', action='store_const', const=42)

            arg_parser.parse_args(['-b'])
            # Namespace(b=42)


    .. py:method:: add_argument_group(title=None, description=None)

        .. code-block:: py

            group = arg_parser.add_argument_group()
            group.add_argument()


    .. py:method:: add_subparsers(title=None, description=None, prog=None, parser_class=None, action=None, option_string=None, dest=None, required=None, help=None, metavar=None)

        .. code-block:: py

            subparsers = arg_parser.add_subparsers(help='subparser')
            first_subparser = subparsers.add_parser()
            first_subparser.add_argument()


    .. py:method:: format_help()
    .. py:method:: format_usage()


    .. py:method:: get_default(key)

        Возвращает значение по умолчанию для ключа


    .. py:method:: parse_args(args=None, namespace=None)

        Парсит аргументы

        .. code-block:: py

            args_parsed = arg_parser.parse_args()


    .. py:method:: print_help()

        Выводит текст с текстом помощи
    

    .. py:method:: print_usage()


    .. py:method:: set_defaults()

        Устанавливает параметры по умолчанию