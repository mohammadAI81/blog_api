from django.urls import path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('blogs', views.Blogs, basename='blog')

urlpatterns = router.urls

# urlpatterns = [
#     path('', views.Blogs.as_view(), name='blogs'),
#     path('<int:pk>/', views.DetailBlog.as_view(), name='edit_blog'),
# ]