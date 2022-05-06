from django.urls import path

from . import views

# recipes:recipe
app_name = 'recipes'

urlpatterns = [
    path('', views.view_home, name='home'),
    path('recipes/<int:id>/', views.view_recipe, name='recipe'),
]
