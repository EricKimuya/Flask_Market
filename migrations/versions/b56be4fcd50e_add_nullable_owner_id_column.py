"""Add nullable owner_id column

Revision ID: b56be4fcd50e
Revises: 
Create Date: 2025-04-08 15:57:44.721893

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b56be4fcd50e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('item', schema=None) as batch_op:
        batch_op.add_column(sa.Column('owner_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_item_owner_id', 'user', ['owner_id'], ['id'])


def downgrade():
    with op.batch_alter_table('item', schema=None) as batch_op:
        batch_op.drop_constraint('fk_item_owner_id', type_='foreignkey')
        batch_op.drop_column('owner_id')
