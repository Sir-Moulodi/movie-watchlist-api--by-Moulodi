from fastapi import FastAPI

app = FastAPI(title="Movie Watchlist API by Moulodi", version="0.0.1")

@app.get("/", tags=["Health Check"])
def health_check():
    """Checks if the API is running."""
    return {"status": "ok", "message": "API is up and running!"}

