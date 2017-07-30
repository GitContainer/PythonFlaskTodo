from sqlalchemy import *
from migrate import *

meta = MetaData()

grant = Table(
    'grants', meta,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id', ondelete='CASCADE')),
    Column('client_id', String, ForeignKey('clients.client_id'), nullable=False),
    Column('code', String, index=True, nullable=False),
    Column('redirect_uri', String),
    Column('expires', DateTime),
    Column('_scopes', Text)
)

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your
    meta.bind = migrate_engine
    grant.create()

def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    grant.drop()
