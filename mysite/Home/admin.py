from Home.models import event
from Home.models import Announcement
from Home.models import Team_event
from Home.models import Team_member
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from Home.models import   Profile
admin.site.register(event)
admin.site.register(Announcement)
admin.site.register(Team_event)
admin.site.register(Team_member)

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# Register your models here.
