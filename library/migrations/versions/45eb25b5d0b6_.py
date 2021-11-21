"""empty message

Revision ID: 45eb25b5d0b6
Revises: eea70e508500
Create Date: 2021-11-21 19:21:17.792902

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45eb25b5d0b6'
down_revision = 'eea70e508500'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'role')
    # ### end Alembic commands ###
