"""random column added

Revision ID: a665b290422d
Revises: 201bf3356f9b
Create Date: 2023-01-19 23:42:39.177598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a665b290422d"
down_revision = "201bf3356f9b"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("blogs", sa.Column("random", sa.String, nullable=True))


def downgrade() -> None:
    op.drop_column("blogs", "random")
