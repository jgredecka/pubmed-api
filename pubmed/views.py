from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings

#Path to the bookmarks file.
bookmarks_path = settings.BASE_DIR / 'pubmed/bookmarks.txt'


# Create your views here.
class ListCreateBookmarks(APIView):
    """
    GET: Get a list of all bookmarked Pubmed IDs from the bookmarks file.
    POST: Add a new bookmark Pubmed ID to bookmarks file.
    """
    def get(self, request, *args, **kwargs):
        file = open(bookmarks_path, 'r')
        bookmarks = file.read()
        bookmarks_list = bookmarks.split(',')
        file.close()
        return Response(bookmarks_list, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        pubmed_id = request.data['pmid']
        file = open(bookmarks_path, 'a')
        file.write(pubmed_id + ',')
        file.close()
        return Response('Bookmark Added', status=status.HTTP_201_CREATED)
        

