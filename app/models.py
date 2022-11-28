from flask_sqlalchemy import SQLAlchemy
from app import db


class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(30))
    user_password = db.Column(db.String(30))
    user_name = db.Column(db.String(30))


class todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(255))
    complete = db.Column(db.Boolean, default = False)