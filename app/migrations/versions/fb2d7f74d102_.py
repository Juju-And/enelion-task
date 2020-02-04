"""empty message

Revision ID: fb2d7f74d102
Revises: 5326d64abdb9
Create Date: 2020-02-04 18:08:12.333502

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'fb2d7f74d102'
down_revision = '5326d64abdb9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('charge_network', 'time_updated')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('charge_network', sa.Column('time_updated', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
