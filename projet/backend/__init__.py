from flask import Flask
from .extensions import mongo
from .main import main
from flask_graphql import GraphQLView
from mongoengine import connect
from flask_graphql_auth import (
    AuthInfoField,
    GraphQLAuth,
    get_jwt_identity,
    create_access_token,
    create_refresh_token,
    query_header_jwt_required,
    mutation_jwt_refresh_token_required,
    mutation_jwt_required
)



connect("projet", host="mongodb://localhost:27017/test1", alias="default")


def create_app(config='backend.settings'):
    app=Flask(__name__)
    app.config['SECRET_KEY'] = 'achak'
    app.config["JWT_SECRET_KEY"] = "achak"
    auth = GraphQLAuth(app)
    app.config.from_object(config)
    mongo.init_app(app)
    app.register_blueprint(main)
    from .schemas.schemas import schema as sc
    view_func = GraphQLView.as_view("graphql", schema=sc, graphiql=True)

    app.add_url_rule("/graphql",view_func=view_func)
    return app
   