"""followers

Revision ID: 083b26f9d403
Revises: 8a42028e31ca
Create Date: 2022-12-18 21:08:45.369111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '083b26f9d403'
down_revision = '8a42028e31ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
