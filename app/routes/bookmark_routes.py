from fastapi import APIRouter, HTTPException
from app.database.db import collection
from app.models.bookmark_model import Bookmark
from bson import ObjectId

router = APIRouter()

@router.post("/bookmarks/")
async def create_bookmark(bookmark: Bookmark):
    new_bookmark = await collection.insert_one(bookmark.dict())
    return {"id": str(new_bookmark.inserted_id)}

@router.get("/bookmarks/")
async def get_bookmarks():
    bookmarks = []
    async for bookmark in collection.find():
        bookmarks.append({
            "id": str(bookmark["_id"]),
            "title": bookmark["title"],
            "url": bookmark["url"],
            "description": bookmark["description"],
        })
    return bookmarks

@router.put("/bookmarks/{bookmark_id}")
async def update_bookmark(bookmark_id: str, bookmark: Bookmark):
    updated = await collection.update_one(
        {"_id": ObjectId(bookmark_id)},
        {"$set": bookmark.dict()}
    )
    if updated.modified_count == 1:
        return {"message": "Bookmark updated"}
    return {"message": "Bookmark not found"}

@router.delete("/bookmarks/{bookmark_id}")
async def delete_bookmark(bookmark_id: str):
    deleted = await collection.delete_one({"_id": ObjectId(bookmark_id)})
    if deleted.deleted_count == 1:
        return {"message": "Bookmark deleted"}
    return {"message": "Bookmark not found"}
