from fastapi import FastAPI

app = FastAPI(title="Movie Watchlist API", version="0.1.0")

@app.get("/", tags=["Health Check"])
def health_check():
    return {"status": "ok"}
