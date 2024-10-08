"""initial

Revision ID: a09517219b6f
Revises: 
Create Date: 2024-10-02 20:43:39.658391

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a09517219b6f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('device_types',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('houses',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('owner_id', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('devices',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('group_id', sa.UUID(), nullable=True),
    sa.Column('house_id', sa.UUID(), nullable=True),
    sa.Column('serial_number', sa.UUID(), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['device_types.id'], ),
    sa.ForeignKeyConstraint(['house_id'], ['houses.id'], ),
    sa.PrimaryKeyConstraint('id', 'serial_number')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('devices')
    op.drop_table('houses')
    op.drop_table('users')
    op.drop_table('device_types')
    # ### end Alembic commands ###
