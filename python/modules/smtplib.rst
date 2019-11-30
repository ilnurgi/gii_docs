.. title:: python smtplib

.. meta::
    :description:
        Справочная информация по python модулю smtplib.
    :keywords:
        python smtplib

.. py:module:: smtplib

smtplib
=======

.. code-block:: py

    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.login(email, password)
    smtp_server.sendmail(sender_email, recipient_email, 'subject text')
    smtp_server.quit()

.. code-block:: sh

    # запуск локального сервера для почты
    $ python -m smtpd -n -c DebuggingServer localhost:1025


SMTP()
------

.. py:class:: SMTP(host, port)

    .. code-block:: py

        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)

        with SMTP('localhost', 1025) as smtp_server:
            pass


    .. py:method:: login(user, password)

        Авторизация на сервисе


    .. py:method:: sendmail(sender, receiver, message)

        Отправляет сообщение на указанную почту


SMTPServerDisconnected()
------------------------

.. py:class:: SMTPServerDisconnected()


SMTPException()
---------------

.. py:class:: SMTPException()


Examples
--------

.. code-block:: py

    # отправка сообщения с html содержимым

    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    text = 'some text'
    message.attach(MIMEText(text, "plain"))

    html = "<html><body>some text</body></html> """
    message.attach(MIMEText(html, "html"))

    with smtplib.SMTP(host, post) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


.. code-block:: py

    # отправка сообщения с файлом

    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    message = MIMEMultipart()
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    text = 'some text'
    message.attach(MIMEText(text, "plain"))

    with open(filename, "rb") as attachment:
        content = attachment.read()

    part = MIMEBase("application", "octet-stream")
    part.set_payload(content)

    encoders.encode_base64(part)

    part.add_header("Content-Disposition", f"attachment; filename= {filename}")
    message.attach(part)

    with smtplib.SMTP(host, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


.. code-block:: py

    # отправка изображения внутри письма

    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    from email.mime.multipart import MIMEMultipart

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    html = "<html><body><img src="cid:myimage"></body></html>"
    message.attach(MIMEText(html, "html"))

    with open(image_name, 'rb') as img:
        image_content = img.read()

    image = MIMEImage(image_content)
    image.add_header('Content-ID', '<myimage>')
    message.attach(image)

    with smtplib.SMTP(host, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


.. code-block:: py

    # отправка изображения внутри письма используя base64

    import base64

    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    from email.mime.multipart import MIMEMultipart

    with open(image_name, 'rb') as img:
        image_content = img.read()

    image_64 = base64.b64encode(image_content).decode()

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    html = f"<html><body><img src="data:image/jpg;base64,{image_64}"></body></html>"
    message.attach(MIMEText(html, "html"))

    with smtplib.SMTP(host, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
