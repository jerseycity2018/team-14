from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'CommunityHub'

urlpatterns = [
    path('', views.HomeView, {}),
]
