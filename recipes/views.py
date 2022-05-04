from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def view_home(request):
    context = {
        'name': 'alexssandry',
    }
    return render(request, 'recipes/home.html', context=context, status=299)


def view_sobre(request):
    # return HttpResponse('Sobre')
    context = {
        'name': 'Alexssandry',
    }
    return render(request, 'recipes/sobre.html', context=context)
