"""added created_at & updated_at fields in blog table

Revision ID: 201bf3356f9b
Revises: aee1b3cda935
Create Date: 2023-01-19 23:34:12.917029

"""
import uuid

from alembic import op
import sqlalchemy as sa
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = "201bf3356f9b"
down_revision = "aee1b3cda935"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "blogs",
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=func.now()),
    )
    op.add_column(
        "blogs",
        sa.Column("updated_at", sa.DateTime(timezone=True), onupdate=func.now()),
    )


def downgrade() -> None:
    op.drop_column("blogs", "created_at")
    op.drop_column("blogs", "updated_at")
