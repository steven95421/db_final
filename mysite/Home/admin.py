from django.contrib import admin
from Home.models import event
from Home.models import Announcement
from Home.models import Team
from Home.models import User
admin.site.register(event)
admin.site.register(Announcement)
admin.site.register(Team)
admin.site.register(User)

# Register your models here.
