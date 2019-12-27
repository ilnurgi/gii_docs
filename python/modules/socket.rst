.. title:: python socket

.. meta::
    :description:
        Справочная информация по python модулю socket.
        Модуль для работы с сокетом.
    :keywords:
        python sockets

.. py:module:: socket

socket
======


AF_INET
-------

.. py:attribute:: AF_INET

    IPv4 протокол

AF_UNIX
-------

.. py:attribute:: AF_UNIX

    Юниксовый сокет

AF_INET6
--------

.. py:attribute:: AF_INET6

    IPv6 протокол


SOCK_DGRAM
----------

.. py:attribute:: SOCK_DGRAM

    UDP протокол


SOCK_STREAM
-----------

.. py:attribute:: SOCK_STREAM

    TCP протокол


SOL_SOCKET
----------

.. py:attribute:: SOL_SOCKET


SO_DROADCAST
------------

.. py:attribute:: SO_DROADCAST


SO_REUSEADDR
------------

.. py:attribute:: SO_REUSEADDR


socket()
--------

.. py:class:: socket()

    Сокет соединение

    .. code-block:: py

        # ipv4 udp
        sock = socket(AF_INET, SOCK_DGRAM)

        # unix socket
        sock = socket(AF_UNIX, SOCK_DGRAM)

        with socket.socket(AF_INET, SOCK_DGRAM) as sock:

            sock.bind(('127.0.0.1', 8888))

            while True:
                sock.bind()

        # ipv4 tcp
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    .. py:method:: accept()

        Ожидает клиентов и возвращает кортеж данных по подключенным клиентам

        .. code-block:: py

            client, addr = sock.accept()
            # client - socket
            # addr - ('127.0.0.1', 63333)

    .. py:method:: bind(bind_param)

        Привязываемся к указанному хосту

        .. code-block:: py

            sock.bind(('127.0.0.1', 8888))
            sock.bind('unix.sock')

    .. py:method:: close()

        Закрывает соединени

        .. code-block:: py

            sock.close()


    .. py:method:: connect()

        Подсоединяется к серверу

        .. code-block:: py

            sock.connect(('127.0.0.1', 8888))
            sock.connect('unix.sock')

    .. py:method:: listen(count)

        Устанавливает размер очереди обработки

        .. code-block:: py

            sock.listen(5)

    .. py:method:: recv(size)

        Блокирует интерпретатор, ожидая данные от клиента

        .. code-block:: py

            result = sock.recv(1024)
            # b'message'


    .. py:method:: sendall(bytes)

        .. code-block:: py

            socket.sendall(b'GET / HTTP/1.0\r\nHost: www.ilnurgi.ru\r\n\r\n')


    .. py:method:: sendTo(message, host)

        Отправляет сообщение по хосту

        .. code-block:: py

            sock.sendTo(b'message', ('127.0.0.1', 8888))
            sock.sendTo(b'message', 'unix.sock')

    .. py:method:: setblocking(block=True)

        Включает/выключает блокирующий режим

        .. code-block:: py

            sock.setblocking(True)

    .. py:method:: setsockopt()

        .. code-block:: py

            sock.setsockopt(SOL_SOCKET, SO_DROADCAST, 1)

            sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    .. py:method:: settimeout(timeout)

        Устанавливает таймаут для подключений

        .. code-block:: py

            sock.settimeout(5)

.. code-block:: py

    """
    работа с блютуз
    """

    import socket

    address, services = socket.bt_obex_discover()

    print(address, services)
    # 00:12:d2:41:35:e4 {"OBEX Object Push":9}

    MY_PC = "00:12:d2:41:35:e4"
    address, services = socket.bt_obex_discover(MY_PC)


.. code-block:: py

    """
    отправка фотографии по БТ
    """

    photo_path = 'photo.jpg'

    address, services = socket.bt_obex_discover()

    if u'OBEX Object Push' in services:
        channel = services[u'OBEX Object Push']
        socket.bt_obex_send_file(address, channel, photo_path)

.. code-block:: py

    """
    простой http server
    """

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9004))
    server_socket.listen()
    while True:
        client_connection, client_address = server_socket.accept()
        request = client_connection.recv(1024)
        print(request)

        client_connection.sendall(b"HTTP/1.1 200 OK\n\nHello!")
        client_connection.close()


.. code-block:: py

    """
    wsgi реализация
    """

    client_connection, client_address = server_socket.accept()
    request = client_connection.recv(1024)
    response = application(request)
    client_connection.sendall(response)
    client_connection.close()
