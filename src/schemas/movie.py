# Written by Amir Hossin Moulodi
from pydantic import Field
from typing import Optional
from uuid import UUID
from archipy.models.dtos.base_dtos import BaseDTO
from src.models.movie import MovieStatus

class MovieBase(BaseDTO):
    title: str = Field(..., min_length=1)
    genre: Optional[str] = None
    release_year: Optional[int] = Field(None, gt=1890, lt=2030)

class MovieCreate(MovieBase):
    status: MovieStatus

class MovieUpdate(BaseDTO):
    status: Optional[MovieStatus] = None
    rating: Optional[int] = Field(None, ge=1, le=5)
    notes: Optional[str] = None

class MovieResponse(MovieBase):
    movie_uuid: UUID
    status: MovieStatus
    rating: Optional[int]
    notes: Optional[str]

class MovieStats(BaseDTO):
    total_movies: int
    watched_movies: int
    want_to_watch_movies: int
    average_rating: Optional[float] = None