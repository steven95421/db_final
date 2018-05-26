from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def events(request):
    return render(request, 'events.html')


def signup(request):
    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')


def anncs(request):
    return render(request, 'anncs.html')


def admin(request):
    return render(request, 'admin.html')
