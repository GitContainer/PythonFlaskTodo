import datetime

from todoapp.models import db

from todoapp.models.base_model import BaseModel

class User(db.Model, BaseModel):
    __tablename__ = 'users'

    readable = ['id', 'first_name', 'last_name', 'email', 'username', 'created_at', 'updated_at']

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    username = db.Column(db.String, index=True, unique=True)
    email = db.Column(db.String, index=True, unique=True)
    password = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, first_name, last_name, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
