from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from .views import login_view, register_view, logout_view, HomeView, UserSurveyFormView, WasteTrackingFormView, VolunteerTrackingFormView
from .views import profileView, AdminDashView, profileHomeView, OneJobView, TaskSampleView,ProgressDemo
app_name = 'CommunityHub'

urlpatterns = [
    path('', HomeView, name = 'home'),
    path('signup/', register_view, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', login_view, name = 'login'),
    path('survey/', UserSurveyFormView, name='survey'),
    path('wasteTrack/', WasteTrackingFormView, name='wasteTrack'),
    path('volunteerTrack/', VolunteerTrackingFormView, name='volunteerTrack'),
    path('profile/', profileHomeView, name = 'profile'),
    path('profile/contrib', profileView, name='contrib'),
    path('dash/',AdminDashView, name = 'adminDash'),
    path('profile/jobex',OneJobView, name='jobExample' ),
    path('dash/tasks', TaskSampleView, name = 'tasks'),
    path('profile/progress', ProgressDemo, name='progress'),
]
