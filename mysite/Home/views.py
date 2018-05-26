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


def register(request):
    return render(request, 'register.html')


def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST, prefix='user')
        upf = UserProfileForm(request.POST, prefix='userprofile')
        if uf.is_valid() * upf.is_valid():
            user = uf.save()
            userprofile = upf.save(commit=False)
            userprofile.user = user
            userprofile.save()
            return django.http.HttpResponseRedirect(…something…)
    else:
        uf = UserForm(prefix='user')
        upf = UserProfileForm(prefix='userprofile')
    return django.shortcuts.render_to_response('register.html',
                                               dict(userform=uf,
                                                    userprofileform=upf),
                                               context_instance=django.template.RequestContext(request))
