from sqlalchemy import *
from migrate import *

meta = MetaData()

user = Table(
    'users', meta,
    Column('id', Integer, primary_key=True)
    Column('first_name', String)
    Column('last_name', String)
    Column('username', String, unique=True, index=True)
    Column('password', String)
    Column('email', String, unique=True, index=True)
    Column('created_at', DateTime)
    Column('updated_at', DateTime)
)

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    user.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    user.drop()
