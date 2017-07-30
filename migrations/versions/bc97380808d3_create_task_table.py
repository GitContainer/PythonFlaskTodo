"""create task table

Revision ID: bc97380808d3
Revises: 
Create Date: 2017-07-30 19:44:56.392714

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc97380808d3'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
	op.create_table(
		'tasks',
		sa.Column('id', sa.Integer, primary_key=True),
		sa.Column('task', sa.String),
		sa.Column('created_at', sa.DateTime),
		sa.Column('updated_at', sa.DateTime),
		)


def downgrade():
    op.drop_table('tasks')
