from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped

from src.adapters.database.tables.base import Base


class User(Base):
    __tablename__ = "url"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    url: Mapped[str] = mapped_column(String(64), nullable=False)
    short_code: Mapped[str] = mapped_column(String(32), nullable=False)
    access_count: Mapped[int] = mapped_column(Integer, nullable=False)

