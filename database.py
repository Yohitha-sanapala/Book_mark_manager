
from motor.motor_asyncio import AsyncIOMotorClient
import os
MONGO_URL = os.getenv("mongo.env")
client = AsyncIOMotorClient(MONGO_URL)
db = client.bookmark_manager  # Database name
collection = db.bookmarks  # Collection name
