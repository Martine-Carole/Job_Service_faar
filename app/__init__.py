from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app() :
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    db.init_app(app)
    migrate.init_app(app, db)
    api = Api(app)

    from app.routes import initialize_routes
    initialize_routes(api)

    return app
