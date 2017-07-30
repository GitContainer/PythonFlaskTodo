import pprint
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from todoapp.models import db

from todoapp.models.base_model import BaseModel
from todoapp.models.token import Token

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
    client = db.relationship("Client")
    # constructor for login
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # constructor for storing new user
    def new_user(self, first_name, last_name, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.set_password(password)
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def check_password(self, user, password):
        return check_password_hash(user.password, password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def authenticate(self, username, password):
        user = self.query.filter_by(username=username).first()
        if user is not None:
            if self.check_password(user, password):
                return user
        return None

    def identity(self, payload):
        user_id = payload['id']
        # user_role = payload['role']
        return self.query.filter(id==user_id).first()

    def hastoken(self):
        token = db.session.query(Token).filter_by(user_id = self.id).first()
        if user is not None:
            if user.access_token:
                return user.access_token
        return None        