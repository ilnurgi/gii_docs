socket
======

Работа с сокетом


.. code-block:: py

    # работа с блютуз
    import socket

    address, services = socket.bt_obex_discover()

    print(address, services)
    # 00:12:d2:41:35:e4 {"OBEX Object Push":9}

    MY_PC = "00:12:d2:41:35:e4"
    address, services = socket.bt_obex_discover(MY_PC)


.. code-block:: py

    # отправка фотографии по БТ

    photo_path = 'photo.jpg'

    address, services = socket.bt_obex_discover()

    if u'OBEX Object Push' in services:
        channel = services[u'OBEX Object Push']
        socket.bt_obex_send_file(address, channel, photo_path)

.. code-block:: py

    # простой http server

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

    # wsgi реализация

    client_connection, client_address = server_socket.accept()
    request = client_connection.recv(1024)
    response = application(request)
    client_connection.sendall(response)
    client_connection.close()