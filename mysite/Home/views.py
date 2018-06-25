from django.shortcuts import render
from django.shortcuts import redirect
from Home.forms import SignUpForm
from django.http import HttpResponse
from Home.models import Announcement
from Home.models import event
from django.contrib.auth import  authenticate
from django.contrib.auth import login as auth_login
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
    return render(request, './registration/login.html')


def anncs(request, id):
    cur_Announcement = Announcement.objects.get(id=id)
    return render(request, 'anncs.html', {'anncs': cur_Announcement})


def admin(request):
    return render(request, 'admin.html')


def add_teammate(request, id):
    return render(request, 'register.html')


def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    user.save()

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user.profile.gender = form.cleaned_data.get('gender')
            user.profile.studnet_name = form.cleaned_data.get('studnet_name')
            auth_login(request,user)
            return redirect('/home/', permanent=True)
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})
def delete_event(request, id):
    event_delete = event.objects.get(id=id)
    event_delete.delete()
    return redirect('/events/', permanent=True)

    


