import os

from django.contrib import messages  # noqa: F401
from django.db.models import F, Q, Value  # noqa
from django.db.models.aggregates import Count, Max, Min  # noqa
from django.db.models.functions import Concat
from django.forms.models import model_to_dict
from django.http import Http404, JsonResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from tag.models import Tag
from utils.pagination import func_pagination

from recipes.models import Recipe

# Create your views here.

PER_PAGE = int(os.environ.get('PER_PAGE', 6))

# print('DEBUG = {0}'.format(os.environ.get('DEBUG')))


def theory(request, *args, **kwargs):
    # Sem usar a query o django não faz consulta na base de dados.

    # recipes = Recipe.objects.all()
    # recipes_filter = recipes.filter(title__icontains='Teste')
    # recipes_first = recipes.first()
    # recipes_first_2 = recipes.filter(title__icontains='Test').first()
    # recipes_last = recipes.last()
    # recipes_order_crescente = recipes.order_by('id')
    # recipes_order_decrescente = recipes.order_by('-id')

    # filter(pk=id) = retornar um objecto com a primary key (id)

    # Recipe.object.all()
    # Recipe.object.get()
    # Recipe.object.filter()
    # Recipe.object.filter().filter().first()

    # print('RECIPES = {0}'.format(recipes))
    # print('RECIPES = {0}'.format(recipes[0].title))

    # list(recipes)

    # recipes = Recipe.objects.filter(
    #     Q(
    #         Q(title__icontains='ena',) |
    #         Q(description__icontains='te',)
    #     )
    # )
    # recipes = recipes.select_related('author')

    # recipes = Recipe.objects.values('id', 'title', 'author__username')
    recipes = Recipe.objects.all().annotate(
        author_full_name=Concat(
            F('author__first_name'),
            Value(' '),
            F('author__last_name'))
    )
    number_of_recipes = recipes.aggregate(Count('id'))

    context = {
        'recipes': recipes,
        'number_of_recipes': number_of_recipes,
    }

    return render(
        request,
        'recipes/pages/theory.html',
        context=context,
    )


class RecipeListViewHome(ListView):
    model = Recipe
    paginate_by = None
    context_object_name = 'recipes'
    ordering = ['-id']
    template_name = 'recipes/pages/home.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)

        qs = qs.filter(
            is_published=True,
        )
        qs = qs.select_related('author', 'category')
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        page_object, pagination_range = func_pagination(
            self.request,
            ctx.get('recipes'),
            pages_per_page=PER_PAGE
        )

        ctx.update({
            'recipes': page_object,
            'pagination_range': pagination_range,
            'link_inicial': '?page=1',
            'link': '?page=',
            'link_final': '?page={0}'.format(
                pagination_range['total_pages']
            )
        })

        return ctx


class RecipeListViewCategory(ListView):
    model = Recipe
    paginate_by = None
    context_object_name = 'recipes'
    ordering = ['-id']
    template_name = 'recipes/pages/category.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        category_id = self.kwargs.get('category_id')

        qs = qs.filter(
            category__id=category_id,
            is_published=True,
        )
        qs = qs.select_related('author', 'category')
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        title = getattr(
            getattr(ctx.get('recipes').first(), 'category', None),
            'name',
            'Not found',
        )

        # Adiciona paginação na tela de category
        page_object, pagination_range = func_pagination(
            self.request, ctx.get('recipes'), pages_per_page=PER_PAGE)

        ctx.update({
            'recipes': page_object,
            'title': '{0}'.format(title),
            'pagination_range': pagination_range,
            'link_inicial': '?page=1',
            'link': '?page=',
            'link_final': '?page={0}'.format(
                pagination_range['total_pages']),
        })

        return ctx


class RecipeListViewSearch(ListView):
    model = Recipe
    paginate_by = None
    context_object_name = 'recipes'
    ordering = ['-id']
    template_name = 'recipes/pages/search.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)

        search_term = self.request.GET.get('q', '')

        qs = qs.filter(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term),
            is_published=True,
        )
        qs = qs.select_related('author', 'category')
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        search_term = self.request.GET.get('q', '')

        page_object, pagination_range = func_pagination(
            self.request, ctx.get('recipes'), pages_per_page=PER_PAGE)

        ctx.update({
            'page_title': 'Search for "{0}"'.format(search_term),
            'recipes': page_object,
            'pagination_range': pagination_range,
            'link_inicial': '?q={0}&page=1'.format(search_term),
            'link': '?q={0}&page='.format(search_term),
            'link_final': '?q={0}&page={1}'.format(
                search_term,
                pagination_range['total_pages']),
        })

        return ctx


def view_home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')

    # messages.success(request, 'ola')
    # messages.warning(request, 'ola')
    # messages.error(request, 'ola')
    # messages.info(request, 'ola')

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


class RecipeDetailViewDetail(DetailView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'recipes/pages/recipe_detail.html'
    pk_url_kwarg = 'recipe_id'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('author', 'category')
        qs = qs.prefetch_related('tags')
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        ctx.update({
            'recipes': [ctx.get('recipes'), ],
            'is_detail_page': True,
        })

        return ctx


def view_recipe_detail(request, recipe_id):
    # recipes = Recipe.objects.filter(id=recipe_id)
    recipe = Recipe.objects.filter(
        pk=recipe_id,
        is_published=True,
    ).first()

    recipe = [recipe, ]

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

    # messages.info(
    #     request, 'You are searching for "{0}"!'.format(search_term))

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


class RecipeListViewHomeAPI(ListView):
    model = Recipe
    paginate_by = None
    context_object_name = 'recipes'
    ordering = ['-id']
    template_name = 'recipes/pages/home.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)

        qs = qs.filter(
            is_published=True,
        )
        qs = qs.select_related('author', 'category')
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        page_object, pagination_range = func_pagination(
            self.request,
            ctx.get('recipes'),
            pages_per_page=PER_PAGE
        )

        ctx.update({
            'recipes': page_object,
            'pagination_range': pagination_range,
            'link_inicial': '?page=1',
            'link': '?page=',
            'link_final': '?page={0}'.format(
                pagination_range['total_pages']
            )
        })

        return {'recipes': ctx.get('recipes')}

    def render_to_response(self, context, **response_kwargs):
        recipe = self.get_queryset().values()
        recipes = self.get_context_data()['recipes']  # noqa
        recipes_dict = self.get_context_data()['recipes'].object_list.values()  # noqa

        return JsonResponse(list(recipe), safe=False)


class RecipeDetailViewDetailAPI(DetailView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'recipes/pages/recipe_detail.html'
    pk_url_kwarg = 'recipe_id'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(pk=self.kwargs.get('recipe_id'))
        qs = qs.select_related('author', 'category')
        qs = qs.prefetch_related('tags')
        return qs

    def render_to_response(self, context, **response_kwargs):
        recipe = self.get_context_data()['recipes']
        recipe_dict = model_to_dict(recipe)

        recipe_dict['cover'] = self.request.build_absolute_uri() + \
            recipe_dict['cover'].url[1:]

        del recipe_dict['is_published']

        return JsonResponse(recipe_dict, safe=False)


class RecipeViewTag(ListView):
    model = Recipe
    paginate_by = None
    context_object_name = 'recipes'
    ordering = ['-id']
    template_name = 'recipes/pages/tag.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            tags__slug=self.kwargs.get('slug', '')
        )

        qs = qs.select_related('author', 'category')
        qs = qs.prefetch_related('tags')

        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        page_title = Tag.objects.filter(
            slug=self.kwargs.get('slug', '')).first()
        if not page_title:
            page_title = 'Not found'

        ctx.update({
            'page_title': '{0}'.format(page_title)
        })

        return ctx
