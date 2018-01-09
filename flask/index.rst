Flask
=====

.. code-block:: py

    from flask import Flask, request

    from flask_wtf import FlaskForm
    from wtforms import StringField, validators


    class ContactForm(FlaskForm):

        name = StringField(
            label='name',
            validators=[
                validators.Length(min=4, max=25)
            ]
        )
        email = StringField(
            label='E-mail',
            validators=[
                validators.Length(min=6, max=35),
                validators.Email()
            ]
        )


    app = Flask(__name__)
    app.config.update(
        DEBUG=TRUE,
        SECRET_KEY='123',
        WTF_CSRF_ENABLED=False
    )

    @app.route('/')
    def home():
        return 'hello world'

    @app.route('/', mehods=['GET', 'POST'])
    def home():
        if request.method == 'POST':
            form = ContactForm(request.form)
            form.validate()
        return 'hello world'

    if __name__ == '__main__':
        app.run()
