# Written by Amir Hossin Moulodi

from uuid import UUID
from sqlalchemy import select, update, delete, func
from sqlalchemy.ext.asyncio import AsyncSession
from archipy.models.errors import NotFoundError

from src.db.session import db_adapter
from src.models.movie import Movie, MovieStatus
from src.schemas.movie import MovieCreate, MovieUpdate

class MovieRepository:
    async def create(self, movie_data: MovieCreate) -> Movie:
        new_movie = Movie(**movie_data.model_dump())
        created_movie = await db_adapter.create(entity=new_movie)
        return created_movie

    async def get_by_id(self, movie_id: UUID) -> Movie | None:
        query = select(Movie).where(Movie.movie_uuid == movie_id)
        result = await db_adapter.execute(statement=query)
        return result.scalar_one_or_none()

    async def get_all(self, skip: int = 0, limit: int = 100) -> list[Movie]:
        query = select(Movie).offset(skip).limit(limit)
        result = await db_adapter.execute(statement=query)
        return result.scalars().all()

    async def update(self, movie_id: UUID, movie_data: MovieUpdate) -> Movie:
        update_data = movie_data.model_dump(exclude_unset=True)
        if not update_data:
            # If there is nothing to update, get and return the movie
            return await self.get_by_id(movie_id)

        query = (
            update(Movie)
            .where(Movie.movie_uuid == movie_id)
            .values(**update_data)
            .returning(Movie)
        )
        result = await db_adapter.execute(statement=query)
        updated_movie = result.scalar_one_or_none()
        if not updated_movie:
            raise NotFoundError(resource_type=Movie.__name__)
        return updated_movie

    async def delete(self, movie_id: UUID) -> bool:
        query = delete(Movie).where(Movie.movie_uuid == movie_id)
        result = await db_adapter.execute(statement=query)
        if result.rowcount == 0:
            raise NotFoundError(resource_type=Movie.__name__)
        return True

    async def get_stats(self) -> dict:
        async with db_adapter.session_manager.get_session() as session:
            total_movies_query = select(func.count()).select_from(Movie)
            total_movies = (await session.execute(total_movies_query)).scalar()

            watched_movies_query = select(func.count()).where(Movie.status == MovieStatus.WATCHED)
            watched_movies = (await session.execute(watched_movies_query)).scalar()

            avg_rating_query = select(func.avg(Movie.rating)).where(Movie.status == MovieStatus.WATCHED)
            avg_rating = (await session.execute(avg_rating_query)).scalar()

        return {
            "total_movies": total_movies or 0,
            "watched_movies": watched_movies or 0,
            "want_to_watch_movies": (total_movies or 0) - (watched_movies or 0),
            "average_rating": avg_rating or 0.0,
        }