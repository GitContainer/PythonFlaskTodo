from sqlalchemy import *
from migrate import *

meta = MetaData()

client = Table(
    'clients', meta,
    Column('client_id', String, primary_key=True),
    Column('name', String),
    Column('description', String),
    Column('client_secret', String, unique=True, index=True, nullable=False),
    Column('is_confidential', Boolean),
    Column('_redirect_uris', Text),
    Column('_default_scopes', Text)
)

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    client.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    client.drop()
