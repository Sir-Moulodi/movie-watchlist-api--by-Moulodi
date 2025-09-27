# Written by Amir Hossin Moulodi
from uuid import UUID
from archipy.helpers.decorators.sqlalchemy_atomic import async_sqlalchemy_atomic_decorator
from archipy.models.errors import InvalidArgumentError
from src.repositories.movie_repository import MovieRepository
from src.schemas.movie import MovieCreate, MovieUpdate, MovieResponse, MovieStats

class MovieService:
    def __init__(self, repository: MovieRepository = MovieRepository()):
        self._repository = repository

    @async_sqlalchemy_atomic_decorator
    async def create_movie(self, movie_data: MovieCreate) -> MovieResponse:
        created_movie = await self._repository.create(movie_data=movie_data)
        return MovieResponse.model_validate(obj=created_movie, from_attributes=True)

    async def get_movie_by_id(self, movie_id: UUID) -> MovieResponse | None:
        movie = await self._repository.get_by_id(movie_id=movie_id)
        if movie:
            return MovieResponse.model_validate(obj=movie, from_attributes=True)
        return None

    async def get_all_movies(self, skip: int, limit: int) -> list[MovieResponse]:
        movies = await self._repository.get_all(skip=skip, limit=limit)
        return [MovieResponse.model_validate(obj=movie, from_attributes=True) for movie in movies]

    @async_sqlalchemy_atomic_decorator
    async def update_movie(self, movie_id: UUID, movie_data: MovieUpdate) -> MovieResponse:
        if movie_data.rating is not None and movie_data.status != "watched":
            raise InvalidArgumentError("Rating can only be set for 'watched' movies.")

        updated_movie = await self._repository.update(movie_id=movie_id, movie_data=movie_data)
        return MovieResponse.model_validate(obj=updated_movie, from_attributes=True)

    @async_sqlalchemy_atomic_decorator
    async def delete_movie(self, movie_id: UUID) -> bool:
        return await self._repository.delete(movie_id=movie_id)

    async def get_movie_stats(self) -> MovieStats:
        stats_data = await self._repository.get_stats()
        return MovieStats(**stats_data)