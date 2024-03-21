from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Blog, Comment
from .serializer import BlogSerializer, CommetSerializer


@api_view(['GET', 'POST'])
def blogs(request):
    queryset_blogs = Blog.objects.filter(published='pub')
    serializer = BlogSerializer(queryset_blogs, many = True)
    return Response(serializer.data)



@api_view(['GET', 'DELETE', 'PUT'])
def detail_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    comments = Comment.objects.filter(post=blog)
    serializer = BlogSerializer(blog)
    serializer_commet = CommetSerializer(comments, many= True)
    return Response(data=[serializer.data, serializer_commet.data])
