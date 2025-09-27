# Written by Amir Hossin Moulodi
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status, Response
from typing import List
from src.services.movie_service import MovieService
from src.schemas.movie import MovieCreate, MovieUpdate, MovieResponse, MovieStats

router = APIRouter()
movie_service = MovieService()

@router.post("/", response_model=MovieResponse, status_code=status.HTTP_201_CREATED)
async def create_movie(movie: MovieCreate):
    return await movie_service.create_movie(movie_data=movie)

@router.get("/", response_model=List[MovieResponse])
async def read_movies(skip: int = 0, limit: int = 100):
    movies = await movie_service.get_all_movies(skip=skip, limit=limit)
    return movies

@router.get("/{movie_id}", response_model=MovieResponse)
async def read_movie(movie_id: UUID):
    db_movie = await movie_service.get_movie_by_id(movie_id=movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie

@router.put("/{movie_id}", response_model=MovieResponse)
async def update_movie(movie_id: UUID, movie: MovieUpdate):
    try:
        return await movie_service.update_movie(movie_id=movie_id, movie_data=movie)
    except Exception as e:
         raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_movie(movie_id: UUID):
    try:
        await movie_service.delete_movie(movie_id=movie_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/stats/", response_model=MovieStats)
async def get_stats():
    return await movie_service.get_movie_stats()