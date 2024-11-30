from django.urls import path, include
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.post_detail, name='post_detail'),
    path('', views.category_posts, name='category_posts')
]
