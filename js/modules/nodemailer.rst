.. title:: js nodemailer

.. meta::
    :description:
        Описание js модуля nodemailer.
    :keywords:
        js nodemailer

nodemailer
==========

https://nodemailer.com/

.. code-block:: sh

    npm install nodemailer


.. code-block:: js

    const nodemailer = require('nodemailer');

    const mailOptions = {from, to, subject, text};

    const transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {user, pass},
    });

    transporter.sendMail(mailOptions, function(error, info){
        if (error) {
            console.log(error);
        } else {
            console.log(info.response);
        }
    });

