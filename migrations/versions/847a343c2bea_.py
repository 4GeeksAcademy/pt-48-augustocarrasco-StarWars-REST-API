"""empty message

Revision ID: 847a343c2bea
Revises: c6af1954c34c
Create Date: 2023-12-14 20:40:12.670231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '847a343c2bea'
down_revision = 'c6af1954c34c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('type', sa.Enum('CHARACTER', 'PLANET', 'STARSHIP', name='itemtype'), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('type')

    # ### end Alembic commands ###
