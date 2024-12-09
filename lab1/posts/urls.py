from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'posts'
urlpatterns = [
    path('', views.posts_list, name="list"),
    path('<slug:slug>', views.post_page, name="page")
]