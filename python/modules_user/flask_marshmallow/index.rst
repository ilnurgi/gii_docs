.. title:: python flask-marshmallow

.. meta::
    :description:
        Справочная информация python модулю flask-marshmallow.
    :keywords:
        python flask-marshmallow

flask-marshmallow
=================

.. code-block:: sh

    pip install flask-marshmallow

.. code-block:: py

    from flask import Flask
    from flask_marshmallow import Marshmallow # new

    app = Flask(__name__)

    ma = Marshmallow(app)


    class PostSchema(ma.Schema):

        class Meta:
            fiels = ('id', 'title', 'content')

    post_schema = PostSchema()
    posts_schema = PostSchema(many=True)
