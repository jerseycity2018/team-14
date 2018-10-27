from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from .views import login_view, register_view, logout_view, HomeView

app_name = 'CommunityHub'

urlpatterns = [
    path('', HomeView, name = 'home'),
    path('signup/', register_view, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', login_view, name = 'login')
]