"""Accidentally deleted db

Revision ID: 882731b52919
Revises: d4867f3a4c0a
Create Date: 2021-01-08 01:18:21.697537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '882731b52919'
down_revision = 'd4867f3a4c0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_item_description', table_name='item')
    op.drop_index('ix_item_id', table_name='item')
    op.drop_index('ix_item_title', table_name='item')
    op.drop_table('item')
    op.add_column('user', sa.Column('pfp_Path', sa.String(), nullable=True))
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('user', 'pfp_Path')
    op.create_table('item',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], name='item_owner_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='item_pkey')
    )
    op.create_index('ix_item_title', 'item', ['title'], unique=False)
    op.create_index('ix_item_id', 'item', ['id'], unique=False)
    op.create_index('ix_item_description', 'item', ['description'], unique=False)
    # ### end Alembic commands ###
