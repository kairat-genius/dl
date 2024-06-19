"""register

Revision ID: 065f79960bd5
Revises: dc5f870833f5
Create Date: 2024-06-17 18:28:31.102264

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '065f79960bd5'
down_revision = 'dc5f870833f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.String(length=200), nullable=False))
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###
