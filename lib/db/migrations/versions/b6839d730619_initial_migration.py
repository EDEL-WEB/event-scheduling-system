"""Initial migration

Revision ID: b6839d730619
Revises: 
Create Date: 2025-05-26 12:10:53.234003

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa



revision: str = 'b6839d730619'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('event_date', sa.DateTime(), nullable=False),
    sa.Column('location', sa.String(length=100), nullable=True),
    sa.Column('organizer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['organizer_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bookings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('booking_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )



def downgrade() -> None:

    op.drop_table('bookings')
    op.drop_table('events')
    op.drop_table('users')
    
