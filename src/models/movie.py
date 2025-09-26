# Written by Amir Hossin Moulodi
import uuid
import enum
from sqlalchemy import Column, String, Integer, DateTime, Enum as SQLAlchemyEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from src.db.session import Base

class MovieStatus(str, enum.Enum):
    WANT_TO_WATCH = "want_to_watch"
    WATCHED = "watched"

class Movie(Base):
    __tablename__ = "movies"
    movie_uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False, index=True)
    # ... بقیه ستون‌ها رو بعدا اضافه می‌کنم