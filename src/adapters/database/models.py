from datetime import datetime
from uuid import UUID

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class URL(Base):
    __tablename__ = "urls"

    id = Column(PGUUID(as_uuid=True), primary_key=True)
    original_url = Column(String, nullable=False)
    short_code = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    access_count = Column(Integer, default=0, nullable=False) 