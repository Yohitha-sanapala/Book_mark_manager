from pydantic import BaseModel

class Bookmark(BaseModel):
    title: str
    url: str
    description: str
