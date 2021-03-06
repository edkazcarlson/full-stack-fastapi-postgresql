"""attempt 5

Revision ID: d50f28cea6e3
Revises: ef54c844fbb8
Create Date: 2021-01-12 19:56:24.374678

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd50f28cea6e3'
down_revision = 'ef54c844fbb8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('AssocTable', sa.Column('left_id', sa.Integer(), nullable=True))
    op.add_column('AssocTable', sa.Column('right_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'AssocTable', 'left', ['left_id'], ['id'])
    op.create_foreign_key(None, 'AssocTable', 'right', ['right_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'AssocTable', type_='foreignkey')
    op.drop_constraint(None, 'AssocTable', type_='foreignkey')
    op.drop_column('AssocTable', 'right_id')
    op.drop_column('AssocTable', 'left_id')
    # ### end Alembic commands ###
