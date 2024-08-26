from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    app.config.from_pyfile('config.py', silent=True)

    db.init_app(app)
    api = Api(app)

    with app.app_context():
        from . import routes, models
        db.create_all()

    return app
