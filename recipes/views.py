from django.shortcuts import render

from recipes.models import Recipe

# from utils.recipes.factory import make_recipe


# Create your views here.


def view_home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')

    # Context para pagina home
    context = {
        'recipes': recipes,
    }
    return render(request, 'recipes/pages/home.html', context=context)


def view_category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True,
    ).order_by('-id')

    title = getattr(
        getattr(recipes.first(), 'category', None),
        'name',
        'Not found',
    )

    context = {
        'recipes': recipes,
        'title': '{0}'.format(title),
    }
    return render(request, 'recipes/pages/category.html', context=context)


def view_recipe_detail(request, recipe_id):
    recipes = Recipe.objects.filter(id=recipe_id)

    context = {
        'recipes': recipes,
        'is_detail_page': True,
    }
    return render(request, 'recipes/pages/recipe_detail.html', context=context)
