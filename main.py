from fastapi import FastAPI, HTTPException
from database import collection
from models import Bookmark
from crud import create_bookmark, get_bookmarks, update_bookmark, delete_bookmark

app = FastAPI(
    title="AI-Powered Bookmark Manager",
    description="API for managing bookmarks with CRUD operations",
    version="1.0",
    docs_url="/docs",  # Default: Swagger UI
    redoc_url="/redoc",  # Alternative API documentation
)

@app.get("/")
async def home():
    return {"message": "Welcome to the AI-Powered Bookmark Manager API"}

@app.post("/bookmarks/")
async def create(bookmark: Bookmark):
    try:
        return await create_bookmark(bookmark)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/bookmarks/")
async def read():
    try:
        return await get_bookmarks()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to fetch bookmarks")

@app.put("/bookmarks/{bookmark_id}")
async def update(bookmark_id: str, bookmark: Bookmark):
    try:
        return await update_bookmark(bookmark_id, bookmark)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid bookmark ID or update failed")

@app.delete("/bookmarks/{bookmark_id}")
async def delete(bookmark_id: str):
    try:
        return await delete_bookmark(bookmark_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid bookmark ID or deletion failed")
