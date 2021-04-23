from django.db import models


class ChannelMessage(models.Model):
    text = models.TextField()
    date = models.DateTimeField()
    sender = models.IntegerField()
    image = models.ImageField()
    views_count = models.IntegerField(default=0)


class Channel(models.Model):
    name = models.CharField(63)
    description = models.TextField()
    admin = models.IntegerField()
    messages = models.ManyToManyField(ChannelMessage)
