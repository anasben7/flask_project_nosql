from flask import Flask
from .extensions import mongo
from .main import main
from flask_graphql import GraphQLView
from mongoengine import connect


def create_app(config='backend.settings'):
    app=Flask(__name__)
    app.config.from_object(config)
    mongo.init_app(app)
    app.register_blueprint(main)
    from .schemas.schemas import schema as sc
    connect("projet", host="mongodb://localhost:27017/test1", alias="default")
    view_func = GraphQLView.as_view("graphql", schema=sc, graphiql=True)

    app.add_url_rule("/graphql",view_func=view_func)
    return app