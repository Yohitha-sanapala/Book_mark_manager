
from pydantic import BaseModel, HttpUrl

class Bookmark(BaseModel):
    title: str
    url: HttpUrl
    description: str
