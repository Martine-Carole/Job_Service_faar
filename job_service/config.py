import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'jobservice.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FIREBASE_CONFIG = {
        "apiKey": "your_api_key",
        "authDomain": "your_project_id.firebaseapp.com",
        "databaseURL": "https://your_project_id.firebaseio.com",
        "projectId": "your_project_id",
        "storageBucket": "your_project_id.appspot.com",
        "messagingSenderId": "your_messaging_sender_id",
        "appId": "your_app_id",
        "measurementId": "your_measurement_id"
    }