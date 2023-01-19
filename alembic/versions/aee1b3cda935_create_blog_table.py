"""create blog table

Revision ID: aee1b3cda935
Revises: 
Create Date: 2023-01-19 21:38:46.653355

"""
import uuid

from alembic import op
import sqlalchemy as sa
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = 'aee1b3cda935'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'blogs'
    )
    sa.Column("id", UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    sa.Column("title", sa.String(), nullable=True)
    sa.Column("description", sa.Text, nullable=True)
    # created_at = sa.Column(sa.DateTime(timezone=True), server_default=func.now())
    # updated_at = sa.Column(sa.DateTime(timezone=True), onupdate=func.now())


def downgrade() -> None:
    op.drop_table("blog")
