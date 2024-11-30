from django.urls import path, include
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('post_detail/', views.post_detail, name='post_detail'),
    path('category_posts/', views.category_posts, name='category_posts')
]
