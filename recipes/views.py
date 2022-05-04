from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def view_home(request):
    return HttpResponse('Home')


def view_sobre(request):
    return HttpResponse('Sobre')
