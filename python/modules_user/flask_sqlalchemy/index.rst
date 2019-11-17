.. title:: python flask-sqlalchemy

.. meta::
    :description:
        Справочная информация python модулю flask-sqlalchemy.
    :keywords:
        python flask-sqlalchemy

flask-sqlalchemy
================

.. code-block:: sh

    pip install flask-sqlalchemy

.. code-block:: py

    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    db = SQLAlchemy(app)

    if __name__ == '__main__':
        app.run(debug=True)

