from flask import Flask
from .extensions import mongo
from .main import main

def create_app(config='backend.settings'):
    app=Flask(__name__)
    app.config.from_object(config)
    mongo.init_app(app)
    app.register_blueprint(main)
    return app