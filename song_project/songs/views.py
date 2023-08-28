from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def songs(request):
    return HttpResponse('Songs will another')