"""users table

Revision ID: 82759ae47820
Revises: 3a66e3715f9e
Create Date: 2024-04-25 16:45:53.864018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82759ae47820'
down_revision = '3a66e3715f9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pronouns', sa.String(length=20), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('pronouns')

    # ### end Alembic commands ###
