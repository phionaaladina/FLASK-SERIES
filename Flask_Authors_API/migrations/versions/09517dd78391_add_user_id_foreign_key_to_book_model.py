"""Add user_id foreign key to Book model

Revision ID: 09517dd78391
Revises: 3b8e9714a3e6
Create Date: 2025-01-03 15:54:59.176279

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09517dd78391'
down_revision = '3b8e9714a3e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
