import requests
from django.shortcuts import render, redirect

BASE_URL = "http://127.0.0.1:8000/bookmarks/"

def bookmark_list(request):
    response = requests.get(BASE_URL)
    bookmarks = response.json()
    return render(request, 'bookmarks.html', {'bookmarks': bookmarks})

def add_bookmark(request):
    if request.method == 'POST':
        title = request.POST['title']
        url = request.POST['url']
        description = request.POST['description']
        requests.post(BASE_URL, params={'title': title, 'url': url, 'description': description})
        return redirect('bookmark_list')
    return render(request, 'add_bookmark.html')

def remove_bookmark(request, bookmark_id):
    requests.delete(f"{BASE_URL}{bookmark_id}")
    return redirect('bookmark_list')
