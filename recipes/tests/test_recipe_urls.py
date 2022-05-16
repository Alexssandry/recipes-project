from django.urls import reverse

from .test_recipe_base import RecipeBaseTest

# Create your tests here.


class RecipeURLsTest(RecipeBaseTest):
    def test_recipe_home_url_is_correct(self):
        home_url = reverse('recipes:home')
        # /
        self.assertEqual(home_url, '/')

    def test_recipe_category_url_is_correct(self):
        category_url = reverse('recipes:category', kwargs={'category_id': 1})
        # /recipes/category/<category_id>
        self.assertEqual(category_url, '/recipes/category/1/')

    def test_recipe_detail_url_is_correct(self):
        detail_url = reverse('recipes:recipe', kwargs={'recipe_id': 1})
        # /recipes/1
        self.assertEqual(detail_url, '/recipes/1/')
