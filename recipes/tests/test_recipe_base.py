from django.test import TestCase
from recipes.models import Category, Recipe, User

# Create your tests here.


class RecipeBaseTest(TestCase):
    def setUp(self) -> None:

        # Cria base de dados para os testes.
        #
        categoria1 = self.make_category()
        categoria2 = self.make_category(name='Assados')
        categoria3 = self.make_category(name='Fritos')
        autor = self.make_author()
        for i in range(45):
            slug = 'recipe-slug1-{0}'.format(i)
            self.make_recipe(autor, categoria1, slug=slug)
        for i in range(18):
            slug = 'recipe-slug2-{0}'.format(i)
            title = 'Assados de carne'
            self.make_recipe(autor, categoria2, title=title, slug=slug)
        for i in range(27):
            slug = 'recipe-slug3-{0}'.format(i)
            self.make_recipe(autor, categoria2, slug=slug)
        for i in range(18):
            slug = 'recipe-slug4-{0}'.format(i)
            self.make_recipe(autor, categoria3, slug=slug, is_published=False)

        return super().setUp()

    def make_category(self, name='Category'):
        return Category.objects.create(name=name)

    def make_author(
        self,
        first_name='user',
        last_name='name',
        username='username',
        password='123456',
        email='username@email.com'
    ):
        return User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )

    def make_recipe(
        self,
        make_author,
        make_category,
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
    ):

        return Recipe.objects.create(  # noqa
            category=make_category,
            author=make_author,
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_step=preparation_step,
            preparation_step_in_html=preparation_step_in_html,
            is_published=is_published,
        )

    def delete_recipe(self, id=1):
        Recipe.objects.get(pk=id).delete()

    def check_recipe_not_published(self, id=1):
        recipes = Recipe.objects.all()
        for recipe in recipes:
            recipe.is_published = False
            recipe.save()

    def delete_recipe_all(self):
        recipes = Recipe.objects.all()
        for recipe in recipes:
            recipe.delete()
