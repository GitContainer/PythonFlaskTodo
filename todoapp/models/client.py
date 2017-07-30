from todoapp.models import db

class Client(db.Model):
    __tablename__ = 'clients'

    name = db.Column(db.String)

    user_id = db.Column(db.ForeignKey('users.id'))

    user = db.relationship('User')

    client_id = db.Column(db.String, primary_key=True)

    client_secret = db.Column(db.String, unique=True, index=True, nullable=False)