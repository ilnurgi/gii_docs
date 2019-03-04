.. py:modules:: SimpleHTTPServer

SimpleHTTPServer
================

.. note::
    
    в 3 ветке перенесен в модуль :py:mod:`http.server`

.. code-block:: py

    import SimpleHTTPServer
    import SocketServer

    PORT = 8000

    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    httpd = SocketServer.TCPServer(("", PORT), Handler)

    print "serving at port", PORT
    httpd.serve_forever()


.. code-block:: sh

    $ python -m SimpleHTTPServer 8000
    Serving HTTP on 0.0.0.0 port 8000 ...