nodemailer
==========

.. code-block:: js

    const nodemailer = require('nodemailer');

    const smtpTransport = nodemailer.createTransport('SMTP', {
        service: 'Gmail',
        auth: {
            user: 'gmail.user@gmail.com',
            pass: 'userpass'
        }
    });

    smtpTransport.sendMail({
        from: 'Ilnurgi Foo <foo@ilnurgi.ru>',
        to: 'bar@ilnurgi.ru, baz@ilnurgi.ru',
        subject: 'Hello',
        text: 'Hello world',
        html: '<b>Hello world </b>'
    }, (error, response){
        if(error){
            console.log(error);
        } else {
            console.log('Message sent: ' + response.message);
        }
        
        smtpTransport.close();
    });