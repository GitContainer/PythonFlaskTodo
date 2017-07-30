"""create token table

Revision ID: 85119812b5c3
Revises: d756d376b5b6
Create Date: 2017-07-30 19:47:20.422784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85119812b5c3'
down_revision = 'd756d376b5b6'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'tokens', 
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, 
            sa.ForeignKey('users.id')),
        sa.Column('client_id', sa.String,
            sa.ForeignKey('clients.id')),
        sa.Column('token_type', sa.String(40), index=True, nullable=False),
        sa.Column('access_token', sa.String),
        sa.Column('refresh_token', sa.String),
        sa.Column('expires', sa.DateTime)
        )


def downgrade():
    op.drop_table('tokens')
