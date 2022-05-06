from django.shortcuts import render
from utils.recipes.factory import make_recipe

# Create your views here.


def view_home(request):
    context = {
        'recipes': [make_recipe() for _ in range(10)],
    }
    return render(request, 'recipes/pages/home.html', context=context)


def view_recipe(request, id):
    context = {
        'recipe': make_recipe(),
        'is_detail_page': True,
    }
    return render(request, 'recipes/pages/recipe-view.html', context=context)
