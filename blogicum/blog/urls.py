from django.urls import path, include
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.post_detail, name='post_detail'),
    path('', views.category_posts, name='category_posts')
]
