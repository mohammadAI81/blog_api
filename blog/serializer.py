from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Comment, Blog



class BlogSerializer(ModelSerializer):
    
    class Meta:
        model = Blog
        fields = ['author', 'title', 'text', 'published']


class CommetSerializer(ModelSerializer):
    body = serializers.CharField(max_length=500, source='comment_text')
    
    class Meta:
        model = Comment
        fields = ['author_comment', 'body', 'post']

