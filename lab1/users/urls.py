from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'users'
urlpatterns = [
    path('register/', views.register_view, name="register"),
        path('login/', views.login_view, name="login"),
]