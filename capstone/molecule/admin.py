from django.contrib import admin
from .models import Group, UserProfile, Message

# Register your models here.

admin.site.register(Group)
admin.site.register(UserProfile)
admin.site.register(Message)
