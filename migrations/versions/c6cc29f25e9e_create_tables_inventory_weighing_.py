"""Create tables Inventory, Weighing, Container

Revision ID: c6cc29f25e9e
Revises: 
Create Date: 2024-02-13 22:21:26.760567

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c6cc29f25e9e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('containers')
    op.drop_table('inventories')
    op.drop_table('weighings')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('weighings',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('value', sa.INTEGER(), nullable=True),
    sa.Column('inventory_id', sa.INTEGER(), nullable=True),
    sa.Column('timestamp', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.ForeignKeyConstraint(['inventory_id'], ['inventories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('inventories',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('start_date', sa.DATE(), nullable=True),
    sa.Column('end_date', sa.DATE(), nullable=True),
    sa.Column('timestamp', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('containers',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('weight', sa.INTEGER(), nullable=True),
    sa.Column('timestamp', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
