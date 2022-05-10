from django.urls import path

from . import views

# recipes:recipe
app_name = 'recipes'

urlpatterns = [
    path('', views.view_home, name='home'),
    path('recipes/category/<int:category_id>',
         views.view_category, name='category'),
    path('recipes/<int:recipe_id>', views.view_recipe_detail, name='recipe'),
]
