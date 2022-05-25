from collections import defaultdict

from django import forms
from recipes.models import Recipe


class AuthorRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['preparation_step'].widget.attrs['class'] = 'span-2'

        self.my_errors = defaultdict(list)

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

        widgets = {
            'cover': forms.FileInput(
                attrs={
                    'class': 'span-2'
                }
            ),
            'preparation_time_unit': forms.Select(
                choices=(
                    ('minutos', 'Minutos'),
                    ('horas', 'Horas'),
                )
            ),
            'servings_unit': forms.Select(
                choices=(
                    ('pessoas', 'Pessoas'),
                    ('pedacos', 'Pedaços'),
                    ('fatias', 'Fatias'),
                    ('porcoes', 'Porções'),
                )
            )
        }

    def clean(self, *args, **kwargs):
        super_clean = super().clean(*args, **kwargs)

        title = self.cleaned_data.get('title')
        if len(title) < 5:
            self.my_errors['title'].append('Must have at least 5 chars.')

        preparation_time = self.cleaned_data.get('preparation_time')
        if preparation_time < 1:
            self.my_errors['preparation_time'].append('Time < 1')

        servings = self.cleaned_data.get('servings')
        if servings < 1:
            self.my_errors['servings'].append('Servings < 1')

        if self.my_errors:
            raise forms.ValidationError(self.my_errors)

        return super_clean
