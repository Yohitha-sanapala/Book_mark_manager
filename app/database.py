from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("mongo")
client = MongoClient(MONGO_URI)
db = client["bookmark_db"]
collection = db["bookmarks"]
