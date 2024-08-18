from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import pyrebase

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
api = Api(app)

firebase = pyrebase.initialize_app(app.config['FIREBASE_CONFIG'])
storage = firebase.storage()

# Import and register routes here
from routes import JobResource, TagResource

if __name__ == '__main__':
    app.run(debug=True)