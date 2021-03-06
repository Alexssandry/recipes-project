from django.urls import path

from . import views

# recipes:recipe
app_name = 'recipes'

urlpatterns = [
     path('', views.RecipeListViewHome.as_view(), name='home'),
     path('recipes/search/', views.RecipeListViewSearch.as_view(), name='search'),  # noqa
     path('recipes/tags/<slug:slug>', views.RecipeViewTag.as_view(), name='tag'),  # noqa
     path('recipes/theory', views.theory, name='theory'),
     path('recipes/api/v1/',
          views.RecipeListViewHomeAPI.as_view(), name='api_home'),
     path('recipes/category/<int:category_id>/',
          views.RecipeListViewCategory.as_view(), name='category'),
     path('recipes/<int:recipe_id>/',
          views.RecipeDetailViewDetail.as_view(), name='recipe'),
     path('recipes/api/v1/<int:recipe_id>/',
          views.RecipeDetailViewDetailAPI.as_view(), name='api_detail'),


]
