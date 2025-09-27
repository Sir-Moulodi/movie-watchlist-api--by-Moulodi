# Written by Amir Hossin Moulodi
from archipy.helpers.decorators.sqlalchemy_atomic import async_sqlalchemy_atomic_decorator
from src.schemas.movie import MovieCreate, MovieResponse

class MovieService:
    def __init__(self):
        # This will be connected to the repository later
        pass

    @async_sqlalchemy_atomic_decorator
    async def create_movie(self, movie_data: MovieCreate) -> MovieResponse:
        """
        This is where the logic to create a new movie will go.
        It uses the atomic decorator from archipy to handle transactions.
        """
        print(f"Logic to create movie '{movie_data.title}' goes here.")
        return None