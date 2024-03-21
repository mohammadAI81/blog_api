from django.urls import path

from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('<int:pk>/', views.detail_blog, name='edit_blog'),
]