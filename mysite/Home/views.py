from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from Home.models import Announcement
from Home.models import event


def home(request):
    Announcement_list = Announcement.objects.all()
    return render(request, 'home.html', {
        'Announcement_list': Announcement_list,
    })


def signup(request, id):
    event_signup = event.objects.get(id=id)
    return render(request, 'signup.html', {'event_signup': event_signup})


def events(request):
    event_list = event.objects.all()
    return render(request, 'events.html', {
        'event_list': event_list,
    })


def login(request):
    return render(request, 'login.html')


def anncs(request):
    return render(request, 'anncs.html')


def admin(request):
    return render(request, 'admin.html')


def register(request):
    return render(request, 'register.html')
