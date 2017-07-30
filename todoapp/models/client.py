from todoapp.models import db

class Client(db.Model):
    __tablename__ = 'clients'

    name = db.Column(db.String)

    description = db.Column(db.String)

    user_id = db.Column(db.ForeignKey('users.id'))

    user = db.relationship('User')

    client_id = db.Column(db.String, primary_key=True)

    client_secret = db.Column(db.String, unique=True, index=True, nullable=False)

    is_confidential = db.Column(db.Boolean)

    _redirect_uris = db.Column(db.Text)
    _default_scopes = db.Column(db.Text)

    @property
    def client_type(self):
        if self.is_confidential:
            return 'confidential'
        return 'public'

    @property
    def redirect_uris(self):
        if self._redirect_uris:
            return self._redirect_uris.split()
        return []

    @property
    def default_redirect_uri(self):
        return self.redirect_uris[0]

    @property
    def default_scopes(self):
        if self._default_scopes:
            return self._default_scopes.split()
        return []