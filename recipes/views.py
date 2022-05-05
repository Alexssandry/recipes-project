from django.shortcuts import render

# Create your views here.


def view_home(request):
    context = {
        'title': 'Recipes',
        'name': 'Alexssandry',
    }
    return render(request, 'recipes/pages/home.html', context=context)
