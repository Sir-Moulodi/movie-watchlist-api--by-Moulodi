# Written by Amir Hossin Moulodi
import uuid
import enum
from sqlalchemy import Column, String, Integer, DateTime, Enum as SQLAlchemyEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from archipy.models.entities import BaseEntity

class MovieStatus(str, enum.Enum):
    WANT_TO_WATCH = "want_to_watch"
    WATCHED = "watched"

class Movie(BaseEntity):
    __tablename__ = "movies"

    movie_uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False, index=True)
    genre = Column(String, nullable=True)
    release_year = Column(Integer, nullable=True)
    status = Column(SQLAlchemyEnum(MovieStatus), nullable=False)
    rating = Column(Integer, nullable=True)
    notes = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())