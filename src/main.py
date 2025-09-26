# Written by Amir Hossin Moulodi
from fastapi import FastAPI

app = FastAPI(title="Movie Watchlist API by Moulodi")

@app.get("/")
def root():
    return {"message": "API is running"}