"""stats

Revision ID: 99643dfdb5c3
Revises: 028dee0924c2
Create Date: 2023-05-10 13:22:13.700388

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "99643dfdb5c3"
down_revision = "028dee0924c2"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("player_stats", sa.Column("combat", sa.Integer(), nullable=True))
    op.add_column("player_stats", sa.Column("offense", sa.Integer(), nullable=True))
    op.add_column("player_stats", sa.Column("defense", sa.Integer(), nullable=True))
    op.add_column("player_stats", sa.Column("support", sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("player_stats", "support")
    op.drop_column("player_stats", "defense")
    op.drop_column("player_stats", "offense")
    op.drop_column("player_stats", "combat")
    # ### end Alembic commands ###
