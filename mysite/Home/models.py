from django.db import models

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


