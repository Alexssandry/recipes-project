from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeBaseTest

# Create your tests here.


class RecipeViewsTest(RecipeBaseTest):

    def test_recipe_home_view_function_is_correct(self):
        view = resolve('/')
        self.assertIs(view.func.__name__, 'view_home')  # views.view_home
        # self.assertIs(view.func, views.view_home)

    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        template = 'recipes/pages/home.html'
        self.assertTemplateUsed(response, template)

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        self.delete_recipe_all()

        # Funciona porque o teste inicia sem dados na base de dados
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('No recipes found here',
                      response.content.decode('utf-8'))

        # # Vou escrever mais coisas
        # self.fail('Preciso terminar de digitar o teste')

    def test_recipe_home_template_loads_recipes(self):
        response = self.client.get(reverse('recipes:home'))

        # Teste feito no context
        # self.assertEqual(len(response.context['recipes']), 1)

        response_content = response.content.decode('utf-8')
        self.assertIn('Recipe title', response_content)

    def test_recipe_home_not_loads_recipes_is_published(self):
        response = self.client.get(reverse('recipes:home'))
        quantidade_recipes_is_published = len(response.context['recipes'])

        self.check_recipe_not_published()

        response = self.client.get(reverse('recipes:home'))
        quantidade_recipes_not_is_published = len(response.context['recipes'])
        self.assertNotEqual(quantidade_recipes_not_is_published,
                            quantidade_recipes_is_published)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve('/recipes/category/1/')
        self.assertIs(view.func, views.view_category)

    def test_recipe_category_view_returns_status_code_200_ok(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertEqual(response.status_code, 200)

    def test_recipe_category_view_loads_correct_template(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1}))
        template = 'recipes/pages/category.html'
        self.assertTemplateUsed(response, template)

    def test_recipe_category_template_shows_no_recipes_found_if_no_recipes(self):  # noqa
        self.delete_recipe_all()

        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1}))
        content = 'No recipes found here.'
        self.assertIn(content, response.content.decode('utf-8'))

    def test_recipe_category_template_loads_recipes(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1}))

        # Teste feito no context
        #  self.assertEqual(
        #     response.context['recipes'].first().title, 'Recipe title')

        # Teste feito se apareceu na pagina
        response_content = response.content.decode('utf-8')
        self.assertIn('Recipe title', response_content)

    def test_recipe_category_not_loads_recipes_is_published(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1}))
        quantidade_recipes_is_published = len(response.context['recipes'])

        self.check_recipe_not_published()

        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1}))
        quantidade_recipes_not_is_published = len(response.context['recipes'])
        self.assertNotEqual(quantidade_recipes_not_is_published,
                            quantidade_recipes_is_published)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve('/recipes/1/')
        self.assertIs(view.func, views.view_recipe_detail)

    def test_recipe_detail_view_returns_status_code_200_ok(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'recipe_id': 1}))
        self.assertEqual(response.status_code, 200)

    def test_recipe_detail_view_loads_correct_template(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'recipe_id': 1}))
        template = 'recipes/pages/recipe_detail.html'
        self.assertTemplateUsed(response, template)

    def test_recipe_detail_template_shows_no_recipes_found_if_no_recipes(self):
        self.delete_recipe()

        response = self.client.get(
            reverse('recipes:recipe', kwargs={'recipe_id': 1}))
        content = 'No recipes found here.'
        self.assertIn(content, response.content.decode('utf-8'))

    def test_recipe_detail_template_loads_recipes(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'recipe_id': 1}))

        # Teste feito no context
        # self.assertEqual(
        #     response.context['recipes'].first().id, 1)

        # Teste feito se apareceu na pagina
        response_content = response.content.decode('utf-8')
        self.assertIn('Recipe title', response_content)

    def test_recipe_detail_not_loads_recipes_is_published(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'recipe_id': 1}))
        quantidade_recipes_is_published = len(response.context['recipes'])

        self.check_recipe_not_published()

        response = self.client.get(
            reverse('recipes:recipe', kwargs={'recipe_id': 1}))
        quantidade_recipes_not_is_published = len(response.context['recipes'])
        self.assertNotEqual(quantidade_recipes_not_is_published,
                            quantidade_recipes_is_published)
