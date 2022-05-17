from django.db.models import Q
from django.http import Http404
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
    # recipes = Recipe.objects.filter(id=recipe_id)
    recipe = Recipe.objects.filter(
        pk=recipe_id,
        is_published=True,
    )

    context = {
        'recipes': recipe,
        'is_detail_page': True,
    }
    return render(request, 'recipes/pages/recipe_detail.html', context=context)


def view_search(request):
    # search_term = request.GET['q']
    search_term = request.GET.get('q', '').strip()
    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
        Q(title__icontains=search_term) |
        Q(description__icontains=search_term),
        is_published=True,
    ).order_by('-id')

    context = {
        'page_title': 'Search for "{0}"'.format(search_term),
        'recipes': recipes,
    }
    return render(request, 'recipes/pages/search.html', context=context)
