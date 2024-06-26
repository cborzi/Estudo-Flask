"""Inclusao de campo respondido na tabela contato

Revision ID: 1dcc502af7eb
Revises: f78e91e7d3f5
Create Date: 2024-04-24 12:55:17.785583

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1dcc502af7eb'
down_revision = 'f78e91e7d3f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contato', schema=None) as batch_op:
        batch_op.add_column(sa.Column('respondido', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contato', schema=None) as batch_op:
        batch_op.drop_column('respondido')

    # ### end Alembic commands ###
