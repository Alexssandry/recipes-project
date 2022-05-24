from django import forms
from recipes.models import Recipe


class AuthorRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'description',
            # 'slug',
            'preparation_time',
            'preparation_time_unit',
            'servings',
            'servings_unit',
            'preparation_step',
            # 'preparation_step_in_html',
            'cover',
            'category',
            # 'author',
        ]
