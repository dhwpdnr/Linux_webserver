from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "User"
    user_id = db.Column(db.String(30))
    user_password = db.Column(db.String(30))
    user_name = db.Column(db.String(30))