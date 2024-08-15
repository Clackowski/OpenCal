from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.utils import timezone

# Create your models here.
class CustomUser(AbstractUser):
    numCals = models.IntegerField(default = 5)
    calendars = models.ManyToManyField('Calendar', related_name='users', blank=True)
    friends = models.ManyToManyField('CustomUser', related_name='friend_set', blank=True)
    
    def __str__(self):
        return self.username
    
class Calendar(models.Model):
    name = models.CharField(max_length=20, default='Calendar Name')
    owner = models.ForeignKey(CustomUser, related_name='owned_calendars', on_delete=models.CASCADE, default=1)
    last_modified = models.DateTimeField(default=timezone.now)
    contributors = models.ManyToManyField('CustomUser', related_name='active_calendars', blank=True)
    
    def __str__(self):
        return self.name
    
class Event(models.Model):
    calendar = models.ForeignKey(Calendar, related_name='events', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    def __str__(self):
        return self.title