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
        self.assertEqual(response.status_code, 200)

    def test_recipe_search_uses_correct_view_funtion(self):
        url = reverse('recipes:search')
        resolved = resolve(url)
        self.assertIs(resolved.func, views.view_search)

    def test_recipe_search_raises_404_if_no_search_term(self):
        # url = reverse('recipes:search') + '?q=++'
        url = reverse('recipes:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
