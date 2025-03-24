import requests
from django.shortcuts import render, redirect
from django.conf import settings  # Import settings for BASE_URL

# Base URL for FastAPI (ensure this is set in settings.py)
FASTAPI_URL = settings.FASTAPI_URL if hasattr(settings, "FASTAPI_URL") else "http://127.0.0.1:8000"

def bookmark_list(request):
    """Fetch all bookmarks from FastAPI and render them in the template."""
    try:
        response = requests.get(f"{FASTAPI_URL}/bookmarks/")
        response.raise_for_status()  # Raise an error if the response is not 200
        bookmarks = response.json()
    except requests.RequestException as e:
        print(f"Error fetching bookmarks: {e}")
        bookmarks = []  # Set empty list if API fails
    return render(request, 'bookmarks.html', {'bookmarks': bookmarks})

def add_bookmark(request):
    """Send a request to FastAPI to create a new bookmark."""
    if request.method == 'POST':
        title = request.POST['title']
        url = request.POST['url']
        description = request.POST['description']
        try:
            response = requests.post(f"{FASTAPI_URL}/bookmarks/", json={
                "title": title,
                "url": url,
                "description": description
            })
            response.raise_for_status()  # Check if request was successful
        except requests.RequestException as e:
            print(f"Error adding bookmark: {e}")
        return redirect('bookmark_list')
    return render(request, 'add_bookmark.html')

def remove_bookmark(request, bookmark_id):
    """Send a request to FastAPI to delete a bookmark."""
    try:
        response = requests.delete(f"{FASTAPI_URL}/bookmarks/{bookmark_id}")
        response.raise_for_status()  # Check if request was successful
    except requests.RequestException as e:
        print(f"Error deleting bookmark: {e}")
    return redirect('bookmark_list')
