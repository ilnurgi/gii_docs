.. py:module:: logging

logging
=======

.. toctree::
    :maxdepth: 1

    config
    

DEBUG
-----

.. py:attribute:: DEBUG


basicConfig()
-------------

.. py:function:: basicConfig(**kwargs)

* datefmt

    Формат строки даты в логах

* level 
    
    Уровень логирования, DEBUG, ERROR, ...    

* filename
* filemode
* format
    
    Форматирование сообщения в логе

    * asctime - время создания сообщения в логах
    * levelname - имя уровня логирования (DEBUG, ERROR, ...)
    * message - пользовательское сообщение
    * name - имя логгера, по умолчанию root
    * process - номер процесса

.. code-block:: py

    logging.basicConfig(
        filename='log.log', 
        filemode='w', 
        format='%(name)s - %(levelname)s - %(message)s',
        level=logging.DEBUG,
        datefmt='%d-%b-%y %H:%M:%S',
    )
    logging.error('Error message')
    # root - ERROR - Error message


critical()
----------

.. py:function:: critical(msg: str)

.. code-block:: py

    logging.critical('Critical message')
    # CRITICAL:root:Critical message


debug()
-------

.. py:function:: debug(msg: str)

.. code-block:: py

    logging.debug('Debug message')


getLogger()
-----------

.. py:function:: getLogger(logger_name: str)

Возвращает :py:class:`logging.Logger()`.

.. code-block:: py

    logger = logging.getLogger('my_logger')
    logger.warning('Warning message')
    # WARNING:my_logger:Warning message

.. code-block:: py

    logger = logging.getLogger(__name__)
    logger.warning('Warning message')
    # WARNING:__main__:Warning message


error()
-------

.. py:function:: error(msg: str, exc_info=False)

Логирование ошибок.

* exc_info
    
    Вывести и трейсбек ошибки, аналогично :py:meth:`logging.exception`

.. code-block:: py

    logging.error('Error message')
    # ERROR:root:Error message

.. code-block:: py

    logging.error('Error message', exc_info=True)
    # ERROR:root:Error message
    Traceback (most recent call last):
      File "script.py", line 16, in <module>
        c = a / b
    ZeroDivisionError: division by zero
    [Finished in 0.1s]


exception()
-----------

.. py:function:: exception(msg: str)

Логирование ошибки с отладочной информацией

.. code-block:: py

    logging.exception('Error message')
    # ERROR:root:Error message
    Traceback (most recent call last):
      File "script.py", line 16, in <module>
        c = a / b
    ZeroDivisionError: division by zero
    [Finished in 0.1s]


info()
------

.. py:function:: info(msg: str)

.. code-block:: py

    logging.info('Info message')


warning()
---------

.. py:function:: warning(msg: str)

.. code-block:: py

    logging.warning('Warning message')
    # WARNING:root:Warning message


FileHandler()
-------------

.. py:class:: FileHandler(file_name: str)

    .. code-block:: py

        file_handler = logging.FileHandler('log.log')

    .. py:method:: setFormatter()

        :py:meth:`Handler.setFormatter()`

    .. py:method:: setLevel()

        :py:meth:`Handler.setLevel()`


Formatter()
-----------

.. py:class:: Formatter()

    Формат сообщения лога

    .. code-block:: py

        fmt = logging.Formatter('%(name)s  %(message)s')


Handler()
---------

.. py:class:: Handler()

    .. py:method:: setLevel(lvl)

        Устанавливает уровень логирования

        .. code-block:: py

            handler.setLevel(logging.DEBUG)

    .. py:method:: setFormatter(fmt: Formatter)

        Устанавливает формат записи лога

        .. code-block:: py

            handler.setFormatter(logging.Formatter('%(name)s  %(message)s'))


Logger()
--------

.. py:class:: Logger()

    Объект логгер, который можно получить через :py:meth:`getLogger`

    .. code-block:: py

        logger = logging.getLogger(__name__)

        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(logging.Formatter('%(name)s - %(message)s')

        logger.addHandler(handler)

    .. py:method:: addHandler(handler: Handler)

        Добавляет обработчик в логгер

        .. code-block:: py

            handler = logging.StreamHandler()
            handler.setLevel(logging.DEBUG)
            handler.setFormatter(logging.Formatter('%(name)s - %(message)s')

            logger.addHandler(handler)

LogRecord()
-----------

.. py:class:: LogRecord()


StreamHandler()
---------------

.. py:class:: StreamHandler()

    .. code-block:: py

        stream_handler = logging.StreamHandler()

    .. py:method:: setFormatter()

        :py:meth:`Handler.setFormatter()`

    .. py:method:: setLevel()

        :py:meth:`Handler.setLevel()`

