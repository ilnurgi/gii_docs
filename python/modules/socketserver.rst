.. py:module:: socketserver

socketserver
============

BaseRequestHandler
------------------

.. py:class:: BaseRequestHandler

    Обработчик запросов

    .. code-block:: py

        class RequestHandler(BaseRequestHandler):

            def handle(self):
                pass

    .. py:attribute:: client_address

        Данные по клиенту

        .. code-block:: py

            self.client_address
            # ('127.0.0.1', 8888)

    .. py:attribute:: request

        Данные и сокет запроса

        .. code-block:: py

            data, socket = self.request


    .. py:method:: finish()
    
    .. py:method:: handle()

        Обработчик запроса    

        .. code-block:: py
    
    .. py:method:: setup()


UDPServer
---------

.. py:class:: UDPServer(conn_param, handler)

    UDP сервер

    .. code-block:: py

        server = UDPServer(('127.0.0.1', 8888), request_handler)

        with UDPServer(('127.0.0.1', 8888), request_handler) as server:
            server.serve_forever()

    .. py:method:: serve_forever()

        Запускает бесконечную обработку запросов

        .. code-block:: py

            server.serve_forever()

TCPServer
---------

.. py:class:: TCPServer(conn_param, handler)

    TCP сервер


ThreadingMixin
--------------

.. py:class:: ThreadingMixin()

    Миксин для обработки запросов по отдельным потокам

    .. code-block:: py

        class MyTreadingServer(ThreadingMixin, TCPServer):
            pass