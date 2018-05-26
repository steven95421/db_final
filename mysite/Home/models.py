from django.db import models
from django.db.models import CharField, Model
from django_mysql.models import ListCharField

# Create your models here.


class event(models.Model):
    Event_name = models.CharField(max_length=50)
    Date = models.DateField()
    Team_Limit = models.IntegerField()
    Team_Size_Limit = models.IntegerField()


class Announcement(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField(blank=True)
    Posted_time = models.CharField(max_length=100)
    image = models.URLField(blank=True)
    markdown_text = models.TextField(blank=True)

class Team(models.Model):
    teamid = models.AutoField(primary_key=True)
    teamname = models.CharField(max_length=100)
    studentid = ListCharField(
        base_field=CharField(max_length=100),
        size=20,
        max_length=(20 * 101)  # 20 * 100 character nominals, plus commas
    )
    studentname = ListCharField(
        base_field=CharField(max_length=100),
        size=20,
        max_length=(20 * 101)  # 20 * 100 character nominals, plus commas
    )
    event = ListCharField(
        base_field=CharField(max_length=100),
        size=20,
        max_length=(20 * 101)  # 20 * 100 character nominals, plus commas
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
class User(models.Model):
	user_id = models.UUIDField(editable=False, unique=True)
	user_password = models.CharField(max_length=20)
	user_email = models.CharField(max_length=100)
	is_admin = models.BooleanField
    
    
