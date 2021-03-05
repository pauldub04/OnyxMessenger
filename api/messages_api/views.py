from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db.models import F
import json

from .models import *


# Create your views here.


def test(request):
    """
    Тестовый метод
    :param request: request
    :return: строка "test"
    """
    return HttpResponse('Test')


def get_dialogues(request):
    """

    :param request: request
    :return: все люди, с кем общается пользователь
    """


def send_message(request):
    """
    Отправить сообщение
    :param request: request.receiver == кому отправляем
    :return:
    """
    #     text = models.TextField()
    #     read = models.BooleanField(default=False)
    #     date = models.DateTimeField(default=0)
    #     sender = models.ForeignKey(to=User, on_delete=models.CASCADE)
    #     receiver = models.IntegerField()
    msg = Message(text=request.GET['text'],
                  read=False,
                  date=timezone.now(),
                  sender=request.user.id,
                  receiver=request.GET['receiver'])
    msg.save()
    return HttpResponse(200)



def get_messages(request):
    """
    Метод для получения сообщений пользователя
    :param request: request.
    :return: жсон всех сообщений между пользователя и человеком
    """
    messages = list(Message.objects.filter(sender=request.user.id)) + list(Message.objects.filter(receiver=request.user.id))
    response = {
        'response': [
            {
                'text': i.text,
                'read': int(i.read),
                'date': i.date,
                'sender': i.sender,
                'receiver': i.receiver
            }
            for i in messages
        ]
    }
    print(response)
    return JsonResponse(response)

