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
