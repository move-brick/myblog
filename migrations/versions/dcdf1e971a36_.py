"""empty message

Revision ID: dcdf1e971a36
Revises: b245668c166a
Create Date: 2018-10-25 18:22:18.820317

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'dcdf1e971a36'
down_revision = 'b245668c166a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('child_cate', 'post_num')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('child_cate', sa.Column('post_num', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    # ### end Alembic commands ###