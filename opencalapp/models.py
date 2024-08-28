from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Account(AbstractUser):
    numCals = models.IntegerField(default = 5)
    calendars = models.ManyToManyField('Calendar', related_name='users', blank=True)
    
    def __str__(self):
        return self.username
    
@receiver(post_save, sender=Account)
def init_friend_list(sender, instance, created, **kwargs):
    if created:
        FriendList.objects.create(user=instance)
    
class Calendar(models.Model):
    name = models.CharField(max_length=20, default='Calendar Name')
    owner = models.ForeignKey(Account, related_name='owned_calendars', on_delete=models.CASCADE, default=1)
    last_modified = models.DateTimeField(default=timezone.now)
    contributors = models.ManyToManyField('Account', related_name='active_calendars', blank=True)
    
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
    
class FriendList(models.Model):
    user = models.OneToOneField('Account', related_name='user', on_delete=models.CASCADE)
    friends = models.ManyToManyField('Account', related_name='friends', blank=True)
    
    def __str__(self):
        return self.user.username
    
    def add_friend(self, userToAdd):
        if userToAdd not in self.friends.all():
            self.friends.add(userToAdd)
            
    def remove_friend(self, userToRemove):
        if userToRemove in self.friends.all():
            self.friends.remove(userToRemove)
            
    def unfriend(self, removee):
        remover_friends_list = self
        remover_friends_list.remove_friend(removee)
        
        friends_list = FriendList.objects.get(user=removee)
        friends_list.remove_friend(self.user)
        
    def is_mutual_friend(self, friend):
        if friend in self.friends.all():
            return True
        else:
            return False
        
class FriendRequest(models.Model):
    sender = models.ForeignKey('Account', related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey('Account', related_name='receiver', on_delete=models.CASCADE)
    is_active = models.BooleanField(blank=True, null=False, default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.sender.username
    
    def accept(self):
        receiver_friend_list = FriendList.objects.get(user=self.receiver)
        if receiver_friend_list:
            receiver_friend_list.add_friend(self.sender)
            sender_friend_list = FriendList.objects.get(user=self.sender)
            if sender_friend_list:
                sender_friend_list.add_friend(self.receiver)
                self.is_active = False
                self.save()
                
    def decline(self):
        self.is_active = False
        self.save()
        
    def cancel(self):
        self.is_active = False
        self.save()