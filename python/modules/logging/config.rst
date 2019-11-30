.. py:module:: logging.config

config
======

Конфигурирование системы логирования

Конфигурация через ini файл

.. code-block:: cfg

    [loggers]
    keys=root,sampleLogger

    [handlers]
    keys=consoleHandler

    [formatters]
    keys=sampleFormatter

    [logger_root]
    level=DEBUG
    handlers=consoleHandler

    [logger_sampleLogger]
    level=DEBUG
    handlers=consoleHandler
    qualname=sampleLogger
    propagate=0

    [handler_consoleHandler]
    class=StreamHandler
    level=DEBUG
    formatter=sampleFormatter
    args=(sys.stdout,)

    [formatter_sampleFormatter]
    format=%(asctime)s - %(name)s - %(levelname)s - %(message)s

Конфигурация через yaml файл

.. code-block:: yaml

    version: 1
    formatters:
      simple:
        format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    handlers:
      console:
        class: logging.StreamHandler
        level: DEBUG
        formatter: simple
        stream: ext://sys.stdout
    loggers:
      sampleLogger:
        level: DEBUG
        handlers: [console]
        propagate: no
    root:
      level: DEBUG
      handlers: [console]


dictConfig()
------------

.. py:function:: dictConfig(cfg_dict: dict)

    Конфигурирование через словарик

    .. code-block:: py

        logging.config.dictConfig(cfg_dict)


fileConfig()
------------

.. py:function:: fileConfig(**kwargs)

    Конфигурирование через файл конфигурации в формате conf

    .. code-block:: py

        logging.config.fileConfig(fname='config.conf', disable_existing_loggers=False)