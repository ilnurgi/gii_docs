.. title:: python signal

.. meta::
    :description: 
        Справочная информация по python модулю signal.
    :keywords: 
        python signal

.. py:module:: signal

signal
======

.. code-block:: py

    import signal

    def receiveSignal(signalNumber, frame):  
        print('Received:', signalNumber)

    # регистрируем перехватываемые сигналы
    signal.signal(signal.SIGHUP, receiveSignal)    
    signal.signal(signal.SIGQUIT, receiveSignal)
    signal.signal(signal.SIGILL, receiveSignal)
    signal.signal(signal.SIGTRAP, receiveSignal)
    signal.signal(signal.SIGABRT, receiveSignal)
    signal.signal(signal.SIGBUS, receiveSignal)
    signal.signal(signal.SIGFPE, receiveSignal)
    #signal.signal(signal.SIGKILL, receiveSignal)
    signal.signal(signal.SIGUSR1, receiveSignal)
    signal.signal(signal.SIGSEGV, receiveSignal)
    signal.signal(signal.SIGUSR2, receiveSignal)
    signal.signal(signal.SIGPIPE, receiveSignal)
    signal.signal(signal.SIGALRM, receiveSignal)
    signal.signal(signal.SIGTERM, receiveSignal)

    # регистрируем сигналы, которые игнорируем
    signal.signal(signal.SIGINT, signal.SIG_IGN)