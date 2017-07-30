from sqlalchemy import *
from migrate import *

meta = MetaData()

token = Table(
    'tokens', meta,
    Column('id', Integer, primary_key=True),
    Column('client_id', String, ForeignKey('clients.client_id'), nullable=False),
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('token_type', String(40)),
    Column('access_token', String, unique=True),
    Column('refresh_token', String, unique=True),
    Column('expires', DateTime),
    Column('_scopes', Text)
)

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    token.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    token.drop()
