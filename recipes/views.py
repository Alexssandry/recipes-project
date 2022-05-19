from django.db.models import Q
from django.http import Http404
from django.shortcuts import render
from utils.pagination import func_pagination

from recipes.models import Recipe

# Create your views here.

PER_PAGE = 9


def view_home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')

    page_object, pagination_range = func_pagination(
        request, recipes, pages_per_page=PER_PAGE)

    # Context para pagina home
    context = {
        'recipes': page_object,
        'pagination_range': pagination_range,
        'link_inicial': '?page=1',
        'link': '?page=',
        'link_final': '?page={0}'.format(
            pagination_range['total_pages']),
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

    # Adiciona paginação na tela de category
    page_object, pagination_range = func_pagination(
        request, recipes, pages_per_page=PER_PAGE)

    context = {
        'recipes': page_object,
        'title': '{0}'.format(title),
        'pagination_range': pagination_range,
        'link_inicial': '?page=1',
        'link': '?page=',
        'link_final': '?page={0}'.format(
            pagination_range['total_pages']),
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

    # Adiciona paginação na tela de category
    page_object, pagination_range = func_pagination(
        request, recipes, pages_per_page=PER_PAGE)

    context = {
        'page_title': 'Search for "{0}"'.format(search_term),
        'recipes': page_object,
        'pagination_range': pagination_range,
        'link_inicial': '?q={0}&page=1'.format(search_term),
        'link': '?q={0}&page='.format(search_term),
        'link_final': '?q={0}&page={1}'.format(
            search_term,
            pagination_range['total_pages']),
    }
    return render(request, 'recipes/pages/search.html', context=context)
