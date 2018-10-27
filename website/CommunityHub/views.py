from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View, TemplateView
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import UserLoginForm, UserRegisterForm, UserSurveyForm, WasteTrackingForm, VolunteerTrackingForm
from .models import WasteTracking, VolunteerTracking

# Create your views here.
def HomeView(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "login.html", context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('CommunityHub:survey')

    context = {
        'form': form,
    }
    return render(request, "signup.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')

def UserSurveyFormView(request):
    next = request.GET.get('next')
    form = UserSurveyForm(request.POST or None)
    if form.is_valid():
        survey = form.save(commit=False)
        survey.user = request.user
        survey.save()
        if next:
            return redirect(next)
        return redirect('/')

    context = {'form': form,}
    return render(request, "form-template.html", context)

def WasteTrackingFormView(request):
    next = request.GET.get('next')
    form = WasteTrackingForm(request.POST or None)
    if form.is_valid():
        survey = form.save(commit=False)
        survey.user = request.user
        survey.save()
        if next:
            return redirect(next)
        return redirect('/')

    context = {'form': form,}
    return render(request, "adminDashForms.html", context)

def VolunteerTrackingFormView(request):
    next = request.GET.get('next')
    form = VolunteerTrackingForm(request.POST or None)
    if form.is_valid():
        survey = form.save(commit=False)
        survey.user = request.user
        survey.save()
        if next:
            return redirect(next)
        return redirect('/')

    context = {'form': form,}
    return render(request, "adminDashForms.html", context)

def profileHomeView(request):
    next = request.GET.get('next')
    if next:
            return redirect(next)
    return render(request, 'profileHome.html')

def profileView(request):
    user = request.user
    waste = WasteTracking.objects.filter(volunteer = user.username)
    volunteer = VolunteerTracking.objects.filter(volunteer = user.username)
    next = request.GET.get('next')
    totalHours = 0
    totalWaste = 0
    
    context = {'waste': waste, 'volunteer': volunteer, 
    'user': user}
    if next:
            return redirect(next)
    return render(request, 'profileContrib.html', context)

def AdminDashView(request):
    user = request.user
    waste = WasteTracking.objects.all()
    volunteer = VolunteerTracking.objects.all()
    next = request.GET.get('next')
    context = {'waste': waste, 'volunteer': volunteer,
    'user': user}
    if next:
            return redirect(next)
    return render(request, 'adminDashboardHome.html', context)

#def OneJobView(request):
#	user = request.user
#	next = request.GET.get('next')
#	return redirect('/job_ex.html')
   
def myKey(e):
    return e.date



