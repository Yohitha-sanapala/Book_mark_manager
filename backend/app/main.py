from fastapi import FastAPI
from app.database import init_db
from app.crud import get_all_bookmarks, add_bookmark, remove_bookmark

app = FastAPI()

@app.on_event("startup")
async def startup_db():
    init_db()

@app.get("/bookmarks/")
async def fetch_bookmarks():
    return get_all_bookmarks()

@app.post("/bookmarks/")
async def create_bookmark(title: str, url: str, description: str):
    return add_bookmark(title, url, description)

@app.delete("/bookmarks/{bookmark_id}")
async def delete_bookmark(bookmark_id: str):
    return remove_bookmark(bookmark_id)
