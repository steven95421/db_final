from django.db import models
import json
import django

# Create your models here.


class event(models.Model):
    #Event_id = models.AutoField(primary_key=True, default=0)
    Event_name = models.CharField(max_length=50)
    Description = models.TextField(blank=True)
    Date = models.DateField()
    Team_Limit = models.IntegerField()
    Team_Size_Limit = models.IntegerField()


class Announcement(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField(blank=True)
    Posted_time = models.CharField(max_length=100)
    image = models.URLField(blank=True)
    markdown_text = models.TextField(blank=True)

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
    event = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    user_id = models.UUIDField(editable=False, unique=True)
    user_password = models.CharField(max_length=20)
    user_email = models.CharField(max_length=100)
    is_admin = models.BooleanField
