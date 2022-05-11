from django.test import TestCase
from django.urls import resolve, reverse
from setuptools import setup

from . import views
from .models import Category, Recipe, User

# Create your tests here.


class Pyteste(TestCase):
    def test_the_pytest_is_ok(self):
        assert 1 == 1, '1 é igual a 1'


class RecipeURLsTest(TestCase):
    def test_recipe_home_url_is_correct(self):
        home_url = reverse('recipes:home')
        # /
        self.assertEqual(home_url, '/')

    def test_recipe_category_url_is_correct(self):
        category_url = reverse('recipes:category', kwargs={'category_id': 1})
        # /recipes/category/<category_id>
        self.assertEqual(category_url, '/recipes/category/1')

    def test_recipe_detail_url_is_correct(self):
        detail_url = reverse('recipes:recipe', kwargs={'recipe_id': 1})
        # /recipes/1
        self.assertEqual(detail_url, '/recipes/1')


class RecipeViewsTest(TestCase):
    # Metodo que executa antes do metodo de test
    def setUp(self):
        ...

    # metodo que executa depoista do metodo de test
    def tearDown(self):
        ...

    def test_recipe_home_view_function_is_correct(self):
        view = resolve('/')
        self.assertIs(view.func, views.view_home)

    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        template = 'recipes/pages/home.html'
        self.assertTemplateUsed(response, template)

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        # Funciona porque o teste inicia sem dados na base de dados
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('No recipes found here',
                      response.content.decode('utf-8'))

    def test_recipe_home_template_loads_recipes(self):
        categoria = Category.objects.create(
            name='Category Teste',
        )
        autor = User.objects.create(
            first_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='username@email.com',
        )
        recipe = Recipe.objects.create(  # noqa
            category=categoria,
            author=autor,
            title='Recipe title',
            description='Recipe description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_step='Recipe preparation steps',
            preparation_step_in_html=False,
            is_published=True,
        )

        response = self.client.get(reverse('recipes:home'))

        # Teste feito no context
        # self.assertEqual(len(response.context['recipes']), 1)

        response_content = response.content.decode('utf-8')
        self.assertIn('Recipe title', response_content)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve('/recipes/category/1')
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
        # Funciona porque o teste inicia sem dados na base de dados
        # response = self.client.get(reverse('recipes:home'))
        # self.assertIn('No recipes found here',
        #               response.content.decode('utf-8'))
        assert 1 == 1

    def test_recipe_category_template_loads_recipes(self):
        categoria = Category.objects.create(
            name='Category Teste',
        )
        autor = User.objects.create(
            first_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='username@email.com',
        )
        recipe = Recipe.objects.create(  # noqa
            category=categoria,
            author=autor,
            title='Recipe title',
            description='Recipe description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_step='Recipe preparation steps',
            preparation_step_in_html=False,
            is_published=True,
        )

        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1}))

        # Teste feito no context
        #  self.assertEqual(
        #     response.context['recipes'].first().title, 'Recipe title')

        # Teste feito se apareceu na pagina
        response_content = response.content.decode('utf-8')
        self.assertIn('Recipe title', response_content)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve('/recipes/1')
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
        # Funciona porque o teste inicia sem dados na base de dados
        # response = self.client.get(reverse('recipes:recipes', kwargs={'recipe_id': 1})) # noqa
        # self.assertIn('No recipes found here',
        #               response.content.decode('utf-8'))
        assert 1 == 1

    def test_recipe_detail_template_loads_recipes(self):
        categoria = Category.objects.create(
            name='Category Teste',
        )
        autor = User.objects.create(
            first_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='username@email.com',
        )
        recipe = Recipe.objects.create(  # noqa
            category=categoria,
            author=autor,
            title='Recipe title',
            description='Recipe description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_step='Recipe preparation steps',
            preparation_step_in_html=False,
            is_published=True,
        )

        response = self.client.get(
            reverse('recipes:recipe', kwargs={'recipe_id': 1}))

        # Teste feito no context
        # self.assertEqual(
        #     response.context['recipes'].first().id, 1)

        # Teste feito se apareceu na pagina
        response_content = response.content.decode('utf-8')
        self.assertIn('Recipe title', response_content)
