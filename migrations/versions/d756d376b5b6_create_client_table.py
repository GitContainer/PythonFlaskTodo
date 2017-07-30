"""create client table

Revision ID: d756d376b5b6
Revises: 25c423d98e73
Create Date: 2017-07-30 19:46:47.364345

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd756d376b5b6'
down_revision = '25c423d98e73'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
    	'clients',
    	sa.Column('client_id', sa.String, primary_key=True),
    	sa.Column('name', sa.String),
    	sa.Column('user_id', sa.Integer,
    		sa.ForeignKey('users.id')),
    	sa.Column('client_secret', sa.String),
    	)


def downgrade():
    op.drop_table('clients')
