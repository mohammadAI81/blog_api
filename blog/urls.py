from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_blog, name='about_blog'),
    path('<int:pk>/', views.detail_blog, name='edit_blog'),
]