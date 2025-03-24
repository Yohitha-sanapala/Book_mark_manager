from django.urls import path
from .views import bookmark_list, add_bookmark, remove_bookmark

urlpatterns = [
    path('bookmarks/', bookmark_list, name='bookmark_list'),
    path('add/', add_bookmark, name='add_bookmark'),
    path('delete/<str:bookmark_id>/', remove_bookmark, name='remove_bookmark'),
]
