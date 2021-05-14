from django.db import models
from django.contrib.auth.models import User


class Channel(models.Model):
    owner = models.ForeignKey(User, related_name='channels', on_delete=models.CASCADE)
    theme = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    icon = models.ImageField()


class Post(models.Model):
    annotation = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    creator_channel = models.ForeignKey(Channel, related_name='posts', on_delete=models.CASCADE)
    icon = models.ImageField()
