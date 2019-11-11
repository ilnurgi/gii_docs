.. title:: python flask-restful

.. meta::
    :description:
        Справочная информация python модулю flask-restful.
    :keywords:
        python flask-restful

flask-restful
=============

.. code-block:: sh

    pip install flask-restful

.. code-block:: py

    from flask import Flask, request
    from flask_restful import Api, Resource

    app = Flask(__name__)
    api = Api(app)

    class PostListResource(Resource):

        def get(self):
            posts = Post.query.all()
            # posts_schema - flask-marshmallow
            return posts_schema.dump(posts)

        def post(self):
            new_post = Post(
                title=request.json['title'],
                content=request.json['content']
            )
            db.session.add(new_post)
            db.session.commit()
            return post_schema.dump(new_post)

    class PostResource(Resource):

        def get(self, post_id):
            post = Post.query.get_or_404(post_id)
            return post_schema.dump(post)

        def patch(self, post_id):
            pass

        def delete(self, post_id):
            pass

    api.add_resource(PostListResource, '/posts')
    api.add_resource(PostResource, '/posts/<int:post_id>')
