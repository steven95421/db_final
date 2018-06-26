from django.db import models
import json
import django
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from mysite import settings
# Create your models here.


class event(models.Model):
    #Event_id = models.AutoField(primary_key=True, default=0)
    Event_name = models.CharField(max_length=50)
    Description = models.TextField(blank=True)
    Date = models.DateTimeField()
    Team_Limit = models.IntegerField()
    Team_Size_Limit = models.IntegerField()

    def __str__(self):
        return self.Event_name


class Announcement(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField(blank=True)
    Posted_time = models.DateTimeField(default=datetime.now, blank=True)
    image = models.URLField(blank=True)
    markdown_text = models.TextField(blank=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.Title


class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=2000)

    def set_studentid(self, x):
        self.studentid = json.dumps(x)

    def get_studentid(self):
        return json.loads(self.student_id)
    student_name = models.CharField(max_length=2000)

    def set_studentname(self, x):
        self.studentname = json.dumps(x)

    def get_studentname(self):
        return json.loads(self.student_name)
    event_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=1, choices=(('m', 'Male'), ('f', 'Female')),
        blank=True, null=True)
    email = models.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.', null=True)

    studnet_name = models.CharField(max_length=2000)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
