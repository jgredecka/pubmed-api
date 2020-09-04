from django.urls import path
from . import views

urlpatterns = [
    path('bookmarks/', views.ListCreateBookmarks.as_view()),
]