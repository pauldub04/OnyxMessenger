from django.http import HttpResponse
from django.http import JsonResponse

from .models import *


def get_channel_messages(request):
    messages = list(ChannelMessage.objects.filter(request.GET['channel_id']))
    response = {
        'response': [
            {
                'text': i.text,
                'date': i.date,
                'sender': i.sender,
                'image': i.image,
                'views_count': i.views_count,
            }
            for i in messages
        ]
    }
    return JsonResponse(response)
