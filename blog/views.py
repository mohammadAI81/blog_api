from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Blog, Comment


@api_view(['GET', 'POST'])
def index(request):

    return Response("Blog List", status=status.HTTP_200_OK)



@api_view(['GET', 'DELETE', 'PUT'])
def detail_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    
    return Response("Hello")


@api_view()
def about_blog(request):

    return Response("Hello")