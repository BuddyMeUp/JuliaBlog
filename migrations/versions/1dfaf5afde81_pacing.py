"""pacing

Revision ID: 1dfaf5afde81
Revises: cfd8b1e79bed
Create Date: 2021-07-21 13:56:21.816727

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1dfaf5afde81'
down_revision = 'cfd8b1e79bed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('budget_pacing',
    sa.Column('category_name', sa.String(length=64), nullable=False),
    sa.Column('category_group_name', sa.String(length=64), nullable=True),
    sa.Column('activity', sa.Float(), nullable=True),
    sa.Column('paced_ideal_spend', sa.Float(), nullable=True),
    sa.Column('daily_amount_target', sa.Float(), nullable=True),
    sa.Column('daily_amount_left', sa.Float(), nullable=True),
    sa.Column('pacing', sa.Float(), nullable=True),
    sa.Column('pacing_perc', sa.Float(), nullable=True),
    sa.Column('average_transaction_amount', sa.Float(), nullable=True),
    sa.Column('transactions_left', sa.Integer(), nullable=True),
    sa.Column('month_progress', sa.Float(), nullable=True),
    sa.Column('transaction_amount_change_perc', sa.Float(), nullable=True),
    sa.Column('transaction_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('category_name')
    )
    with op.batch_alter_table('budget_pacing', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_budget_pacing_category_name'), ['category_name'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('budget_pacing', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_budget_pacing_category_name'))

    op.drop_table('budget_pacing')
    # ### end Alembic commands ###
