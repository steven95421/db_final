from django.shortcuts import render
from django.shortcuts import redirect
from Home.forms import SignUpForm
from django.http import HttpResponse
from Home.models import Announcement
from Home.models import event
from Home.models import Team_event
from Home.models import Team_member
from django.contrib.auth import  authenticate
from django.contrib.auth import login as auth_login
from Home.forms import EventForm
from Home.forms import EventSignUp
from Home.forms import MemberFormset
from django.contrib.auth.models import User
from django.http import JsonResponse

def home(request):
    Announcement_list = Announcement.objects.all()
    return render(request, 'home.html', {
        'Announcement_list': Announcement_list,
    })


def signup(request, id):
    event_signup = event.objects.get(id=id)
    remain_team = event_signup.Team_Limit
    if request.method == 'GET':
        form = EventSignUp(request.GET or None)
        formset = MemberFormset(queryset=Team_member.objects.none())
    elif request.method == 'POST':
        form = EventSignUp(request.POST)
        formset = MemberFormset(request.POST)
        if form.is_valid() and formset.is_valid():
            complete_form = form.save(commit=False)
            complete_form.event_id = id
            complete_form.save()
            for subform in formset:
                member = subform.save(commit=False)
                member.team = complete_form
                member.save()
            return redirect('/events/',permanent=True)
    return render(request, 'signup.html',{'form': form,'event_signup': event_signup,'formset': formset,},)


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


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username=username).exists()
    }
    return JsonResponse(data)

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
    



def events_edit(request, id):
    post = event.objects.get(id=id)
    if request.method == "POST":
        form = EventForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/events/', permanent=True)
    else:
        form = EventForm(instance=post)
    return render(request, 'event_edit.html', {'form': form})

def events_add(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/events/', permanent=True)
    else:
        form = EventForm()
    return render(request, 'event_add.html', {'form': form})

    


