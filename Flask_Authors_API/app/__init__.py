from flask import Flask
from app.extensions import db

def create_app():
    #application factory function
    app = Flask (__name__)

    db.init_app(app)

    @app.route('/')
    def home():
        return 'Authors API Flask Project 1'
    
    return app