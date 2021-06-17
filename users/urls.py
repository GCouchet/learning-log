"""Defines URL patterns for learning_logs."""
from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # hay varias urls que tiene django para usuarios, login, logout, etc
    path('', include('django.contrib.auth.urls')),
    # registration page
    path('register/', views.register, name='register'),
    ]
