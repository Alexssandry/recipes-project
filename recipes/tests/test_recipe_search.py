from unittest import skip

from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeBaseTest

# Create your tests here.


class SearchTest(RecipeBaseTest):
    def test_recipe_search_url_is_correct(self):
        search_url = reverse('recipes:search')
        self.assertEqual(search_url, '/recipes/search/')

    def test_recipe_search_loads_correct_template(self):
        url = reverse('recipes:search') + '?q=teste'
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    @skip('1')
    def test_recipe_search_uses_correct_view_funtion(self):
        url = reverse('recipes:search')
        resolved = resolve(url)
        self.assertIs(resolved.func, views.view_search)

    @skip('2')
    def test_recipe_search_raises_404_if_no_search_term(self):
        # url = reverse('recipes:search') + '?q=++'
        url = reverse('recipes:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_recipe_search_term_is_on_page_title_and_escade(self):
        url = reverse('recipes:search') + '?q=teste'
        response = self.client.get(url)

        self.assertIn(
            'Search for &quot;teste&quot;',
            response.content.decode('utf-8')
        )
