from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def test(request):
    """
    Тестовый метод
    :param request: request
    :return: строка "test"
    """
    return HttpResponse('Test')

