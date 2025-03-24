import requests

FASTAPI_BASE_URL = "http://127.0.0.1:8000"  # Change this if your FastAPI is hosted online

def get_bookmarks():
    response = requests.get(f"{FASTAPI_BASE_URL}/bookmarks/")
    return response.json()

def create_bookmark(title, url, description):
    data = {"title": title, "url": url, "description": description}
    response = requests.post(f"{FASTAPI_BASE_URL}/bookmarks/", json=data)
    return response.json()

def update_bookmark(bookmark_id, title, url, description):
    data = {"title": title, "url": url, "description": description}
    response = requests.put(f"{FASTAPI_BASE_URL}/bookmarks/{bookmark_id}", json=data)
    return response.json()

def delete_bookmark(bookmark_id):
    response = requests.delete(f"{FASTAPI_BASE_URL}/bookmarks/{bookmark_id}")
    return response.json()
