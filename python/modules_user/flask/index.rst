.. title:: python flask

.. meta::
    :description:
        Справочная информация python модулю flask.
    :keywords:
        python flask

flask
=====

.. code-block:: sh

    pip install flask


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

.. py:module:: flask

.. code-block:: shell

    pip install flask

.. code-block:: py

    from flask import Flask, render_template, request
    app = Flask(__name__, static_folder='.', static_url_path='')

    @app.route('/')
    def home():
        return app.send_static_file('index.html')

    @app.route('/')
    def home2():
        return render_template('index.html', **{})

    @app.route('/<idi>')
    def echo(idi):
        return "id = {0}".format(idi)

    @app.route('/')
    def echo2():
        return "id = {0}".format(request.args.get("idi"))

    app.run(port=9999, debug=True)