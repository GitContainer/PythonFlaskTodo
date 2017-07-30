"""create user table

Revision ID: 25c423d98e73
Revises: bc97380808d3
Create Date: 2017-07-30 19:46:17.579020

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25c423d98e73'
down_revision = 'bc97380808d3'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
		'users',
		sa.Column('id', sa.Integer, primary_key=True),
		sa.Column('first_name', sa.String),
		sa.Column('last_name', sa.String),
		sa.Column('username', sa.String),
		sa.Column('email', sa.String),
		sa.Column('password', sa.String),
		sa.Column('created_at', sa.DateTime),
		sa.Column('updated_at', sa.DateTime),
		)


def downgrade():
    op.drop_table('users')

