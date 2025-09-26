from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from app.models.movie import MovieStatus

class MovieBase(BaseModel):
    title: str = Field(..., min_length=1)
    genre: Optional[str] = None
    release_year: Optional[int] = Field(None, gt=1890, lt=2030)

class MovieCreate(MovieBase):
    status: MovieStatus

class MovieUpdate(BaseModel):
    status: Optional[MovieStatus] = None
    rating: Optional[int] = Field(None, ge=1, le=5)
    notes: Optional[str] = None

class MovieResponse(MovieBase):
    movie_uuid: UUID
    status: MovieStatus
    rating: Optional[int]
    notes: Optional[str]

    class Config:
        orm_mode = True

class MovieStats(BaseModel):
    total_movies: int
    watched_movies: int
    want_to_watch_movies: int
    average_rating: Optional[float] = None