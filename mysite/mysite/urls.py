"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from django.urls import path, re_path
from django.conf.urls import url
from Home import views as Home_views  # new
from django.conf.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url='home/')),  # new
    path('home/', Home_views.home),  # new
    path('login/', Home_views.login),
    path('events/', Home_views.events),
    path('events/add', Home_views.events_add),
    path('anncs/add', Home_views.anncs_add),
    re_path('anncs/delete/(?P<id>\d+)/', Home_views.anncs_delete),
    re_path('anncs/edit/(?P<id>\d+)/',  Home_views.anncs_edit),
    re_path('events/edit/(?P<id>\d+)/',  Home_views.events_edit),
    re_path('signup/(?P<id>\d+)/', Home_views.signup),
    re_path('anncs/(?P<id>\d+)/', Home_views.anncs),
    path('register/', Home_views.register),
    re_path('events/delete/(?P<id>\d+)/', Home_views.delete_event),
    path('ajax/validate_username/',
        Home_views.validate_username, name='validate_username'),

]
