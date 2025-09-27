# Written by Amir Hossin Moulodi
from fastapi import FastAPI
from src.api.v1.endpoints import movies

app = FastAPI(title="Movie Watchlist API by Moulodi")

app.include_router(movies.router, prefix="/api/v1/movies", tags=["Movies"])

@app.get("/", tags=["Health Checkinf"])
def root():
    return {"message": "API is running"}