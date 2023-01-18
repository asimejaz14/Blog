import uuid
from uuid import uuid4

from sqlalchemy import Column, Text, String, DateTime
from sqlalchemy.dialects.postgresql import UUID

from database import Base


class Blog(Base):
    __tablename__ = "blogs"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    title = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __str__(self):
        return self.title


