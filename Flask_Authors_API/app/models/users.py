from app.extensions import db

class User(db.Model):
    __tablename__ = 'users' 
    id = db.Column()

    