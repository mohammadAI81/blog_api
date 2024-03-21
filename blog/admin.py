from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.admin import TabularInline

from .models import Blog, Comment
# Register your models here.

class CommetBlog(TabularInline):
    model = Comment
    extra = 1


@admin.register(Blog)
class BlogAdmin(ModelAdmin):
    list_display = ('title', 'author', 'published')
    list_per_page = 10
    list_display_links = ('title',)
    list_filter = ('title', 'published')
    list_editable = ('author', 'published')
    inlines = [
        CommetBlog
    ]

@admin.register(Comment)
class CommentsAdmin(ModelAdmin):
    list_display = ('author_comment', 'post', 'date_created')
    list_filter = ('post',)
    list_per_page = 35
    list_display_links = ('post', 'author_comment')

