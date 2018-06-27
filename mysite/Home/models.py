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


class Team_event(models.Model):
    team = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=100)
    event_id = models.IntegerField()
    def __str__(self):
        return str(self.team)

class Team_member(models.Model):
    team = models.ForeignKey(Team_event, on_delete=models.PROTECT)
    student_id = models.CharField(max_length=2000)
    def __str__(self):
        return self.student_id

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
