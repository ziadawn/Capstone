from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contacts = models.ManyToManyField(User, related_name='contact_groups', blank=True)


# need one-to-one here to connect to users
class UserProfile(models.Model):
    image = models.ImageField(null=True, blank=True)
    bio = models.TextField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    # this function makes the admin panel display the user name rather than a genearic name
    def __str__(self):
        return self.user.username


class Message(models.Model):
    text = models.CharField(max_length=500)
    sender = models.ForeignKey(User)
    recipient = models.ForeignKey(User, null=True, related_name='+')
    group = models.ForeignKey(Group, null=True)
