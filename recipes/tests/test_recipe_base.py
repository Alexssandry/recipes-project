from django.test import TestCase
from recipes.models import Category, Recipe, User

# Create your tests here.


class RecipeBaseTest(TestCase):
    def setUp(self) -> None:

        # Cria base de dados para os testes.
        #
        categoria = self.make_category()
        autor = self.make_author()
        self.make_recipe(autor, categoria)

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
        recipe = Recipe.objects.get(pk=id)
        recipe.is_published = False
        recipe.save()
