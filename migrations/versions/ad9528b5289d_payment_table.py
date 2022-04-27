"""payment table

Revision ID: ad9528b5289d
Revises: 
Create Date: 2022-04-22 23:37:33.414024

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad9528b5289d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('payment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('card_type', sa.String(length=32), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('expiration_month', sa.Integer(), nullable=True),
    sa.Column('expiration_year', sa.Integer(), nullable=True),
    sa.Column('cvv', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('currency', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payment')
    # ### end Alembic commands ###