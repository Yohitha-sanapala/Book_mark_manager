from django.shortcuts import render, redirect
from .fastapi_service import get_bookmarks, create_bookmark, update_bookmark, delete_bookmark

def bookmark_list(request):
    bookmarks = get_bookmarks()
    return render(request, 'bookmarks.html', {'bookmarks': bookmarks})

def add_bookmark(request):
    if request.method == 'POST':
        title = request.POST['title']
        url = request.POST['url']
        description = request.POST['description']
        create_bookmark(title, url, description)
        return redirect('bookmark_list')
    return render(request, 'add_bookmark.html')

def remove_bookmark(request, bookmark_id):
    delete_bookmark(bookmark_id)
    return redirect('bookmark_list')
