from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .models import Blog, Comment
from .serializer import BlogSerializer, CommetSerializer


class Blogs(ModelViewSet):
    queryset = Blog.objects.filter(published='pub')
    serializer_class = BlogSerializer
    

# class Blogs(APIView):
#     def get(self, request):
#         blogs = Blog.objects.filter(published = 'pub')
#         serializer = BlogSerializer(blogs, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = BlogSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         print(serializer.validated_data)
#         serializer.save()
#         return Response(serializer.data)


# class DetailBlog(APIView):
#     def get(self, request, pk):
#         blog = get_object_or_404(Blog, pk=pk)
#         comments = Comment.objects.filter(post=blog)
#         serializer = BlogSerializer(blog)
#         serializer_ = CommetSerializer(comments, many= True)
#         return Response(serializer.data)
    
#     def delete(self, request, pk):
#         blog = get_object_or_404(Blog, pk=pk)
#         blog.delete()
#         return Response({'Delete': 'Not Defind'}, status=status.HTTP_204_NO_CONTENT)
    
#     def patch(self, request):
#         serializer = BlogSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
