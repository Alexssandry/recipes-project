from django.db.models import Q
from django.urls import reverse
from recipes.models import Recipe

from .test_recipe_base import RecipeBaseTest

# Create your tests here.


class PaginationTest(RecipeBaseTest):
    def test_pagination_view_home_is_correct(self):
        recipes = Recipe.objects.filter(is_published=True)
        quantidade_paginas = int(len(recipes) / 9)

        response = self.client.get(reverse('recipes:home'))
        quantidade_context = response.context['recipes'].paginator.num_pages

        self.assertEqual(quantidade_paginas, quantidade_context)

    def test_pagination_view_home_content_is_correct(self):
        recipes = Recipe.objects.filter(is_published=True)
        quantidade_paginas = int(len(recipes) / 9)

        response = self.client.get(reverse('recipes:home'))
        response_content = response.content.decode('utf-8')

        self.assertIn('?page={0}'.format(
            quantidade_paginas),
            response_content
        )

    def test_pagination_view_category_is_correct(self):
        recipes = Recipe.objects.filter(
            is_published=True, category__name='Assados')
        quantidade_paginas = int(len(recipes) / 9)

        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1}))
        quantidade_context = response.context['recipes'].paginator.num_pages

        self.assertEqual(quantidade_paginas, quantidade_context)

    def test_pagination_view_category_content_is_correct(self):
        recipes = Recipe.objects.filter(
            is_published=True, category__name='Assados')
        quantidade_paginas = int(len(recipes) / 9)

        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 2}))
        response_content = response.content.decode('utf-8')

        self.assertIn('?page={0}'.format(
            quantidade_paginas),
            response_content
        )

    def test_pagination_view_search_is_correct(self):
        search_term = 'carne'
        recipes = Recipe.objects.filter(
            Q(title__icontains=search_term),
            is_published=True,
        )
        quantidade_paginas = int(len(recipes) / 9)

        url = reverse('recipes:search') + '?q={0}'.format(search_term)
        response = self.client.get(url)
        quantidade_context = response.context['recipes'].paginator.num_pages

        self.assertEqual(quantidade_paginas, quantidade_context)

    def test_pagination_view_search_content_is_correct(self):
        search_term = 'carne'
        recipes = Recipe.objects.filter(
            Q(title__icontains=search_term),
            is_published=True,
        )
        quantidade_paginas = int(len(recipes) / 9)

        url = reverse('recipes:search') + '?q={0}'.format(search_term)
        response = self.client.get(url)
        response_content = response.content.decode('utf-8')

        self.assertIn('?q={0}&amp;page={1}'.format(
            search_term,
            quantidade_paginas),
            response_content,
        )
