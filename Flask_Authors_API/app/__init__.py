from flask import Flask
from app.extensions import db, migrate

def create_app():
    #application factory function
    app = Flask (__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    #importing and registering models
    from app.models.users import User
    from app.models.companies import Company
    from app.models.books import Book

    @app.route('/')
    def home():
        return 'Authors API Flask Project 1'
    
    return app