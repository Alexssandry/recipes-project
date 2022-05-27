from django.urls import path

from . import views

# recipes:recipe
app_name = 'recipes'

urlpatterns = [
    path('', views.RecipeListViewHome.as_view(), name='home'),
    path('recipes/search/', views.RecipeListViewSearch.as_view(), name='search'),  # noqa
    path('recipes/category/<int:category_id>/',
         views.RecipeListViewCategory.as_view(), name='category'),
    path('recipes/<int:recipe_id>/',
         views.RecipeDetailViewDetail.as_view(), name='recipe'),
]
