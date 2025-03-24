import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv("mongo.env")

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["bookmark_db"]
collection = db["bookmarks"]

def init_db():
    print("Database initialized successfully")
