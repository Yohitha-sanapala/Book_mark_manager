from .database import collection
from .models import Bookmark
from bson import ObjectId

def get_all_bookmarks():
    return list(collection.find({}, {"_id": 1, "title": 1, "url": 1, "description": 1}))

def create_bookmark(bookmark: Bookmark):
    new_bookmark = bookmark.dict()
    collection.insert_one(new_bookmark)
    return new_bookmark

def delete_bookmark(bookmark_id: str):
    collection.delete_one({"_id": ObjectId(bookmark_id)})
    return {"message": "Bookmark deleted"}
