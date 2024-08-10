from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    numCals = models.IntegerField(default = 5)
    isFriend = models.BooleanField(default = True)
    calendars = models.ManyToManyField('Calendar', related_name='users', blank=True)
    
    def __str__(self):
        return self.username
    
    
    
class Calendar(models.Model):
    daysBusy = models.IntegerField(default= 26)
    
    def __str__(self):
        return f"Calendar with {self.daysBusy} days busy"