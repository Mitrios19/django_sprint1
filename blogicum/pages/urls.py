from django.urls import path, include
from . import views


app_name = 'pages'

urlpatterns = [
    path('', views.about, name='about'),
    path('', views.rules, name='rules')
]
