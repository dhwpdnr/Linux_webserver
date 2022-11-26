from flask_sqlalchemy import SQLAlchemy
from app import db


class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(30))
    user_password = db.Column(db.String(30))
    user_name = db.Column(db.String(30))