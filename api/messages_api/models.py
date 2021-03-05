from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.utils import timezone


class Message(models.Model):
    """
    Базовый класс сообщения

    :text: Текст сообщения
    :date: Дата отправки
    :read: прочитано ли сообщение (возможно стоит поменять на status)
    :sender: Пользователь, который отправил сообщение
    :receiver: Пользователь, которому отправляется сообщение, я что то не так сделал, но пока и так сойдет
    Скорее всего надо добавить вместо receiver chat_receiver
    """
    text = models.TextField()
    read = models.BooleanField(default=False)
    date = models.DateTimeField(default=0)
    sender = models.IntegerField()
    receiver = models.IntegerField()

