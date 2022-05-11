from recipes.models import Recipe

from .test_recipe_base import RecipeBaseTest

# Create your test here.


class RecipeModelTest(RecipeBaseTest):
    def receita(self):
        return Recipe.objects.get(pk=1)

    def test_title_is_correct(self):
        recipe = self.receita()
        len_title = len(recipe.title)
        assert len_title <= 65

    def test_description_is_correct(self):
        recipe = self.receita()
        len_description = len(recipe.description)
        assert len_description <= 65

    def test_preparation_time_is_correct(self):
        recipe = self.receita()
        preparation_time = int(recipe.preparation_time)
        assert preparation_time > 0

    def test_preparation_time_unit_is_correct(self):
        recipe = self.receita()
        time_unit = recipe.preparation_time_unit
        list_units = [
            'Minuto',
            'Minutos',
            'Hora',
            'Horas',
        ]
        assert time_unit in list_units

    def test_servings_is_correct(self):
        recipe = self.receita()
        servings = recipe.servings
        assert servings > 0

    def test_servings_unit_is_correct(self):
        recipe = self.receita()
        servings_unit = recipe.servings_unit
        list_units = [
            'Porção',
            'Porções',
            'Pedaço',
            'Pedaços',
            'Fatia',
            'Fatias',
            'Pessoa',
            'Pessoas',
        ]
        assert servings_unit in list_units


class CategoryModelTest(RecipeBaseTest):
    def receita(self):
        return Recipe.objects.get(pk=1)

    def test_name_category_is_correct(self):
        category = self.receita()
        len_category = len(category.category.name)
        assert len_category <= 65
