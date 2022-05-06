from django.shortcuts import render

# Create your views here.


def view_home(request):
    context = {
        'title': 'Recipes',
        'name': 'Alexssandry',
    }
    return render(request, 'recipes/pages/home.html', context=context)


def view_recipe(request, id):
    context = {
        'title': 'Recipes Details',
    }
    return render(request, 'recipes/pages/recipe-view.html', context=context)
