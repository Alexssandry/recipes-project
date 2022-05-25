from django.urls import path

from . import views

# authors:register
app_name = 'authors'

urlpatterns = [
    path('register/', views.view_register, name='register'),
    path('register/create/', views.view_register_create, name='register_create'),  # noqa: E501
    path('login/', views.view_login, name='login'),
    path('login/create/', views.view_login_create, name='login_create'),
    path('logout/', views.view_logout, name='logout'),
    path('dashboard/', views.view_dashboard, name='dashboard'),
    path('dashboard/recipe/<int:id>/edit/',
         views.view_dashboard_recipe_edit, name='dashboard_recipe_edit'),
    path('dashboard/recipe/delete/',
         views.view_dashboard_recipe_delete, name='dashboard_recipe_delete'),
    path('dashboard/recipe/new/', views.view_dashboard_new_recipe,
         name='dashboard_new_recipe'),
    path('dashboard/recipe/new/create/', views.view_dashboard_create_new_recipe,  # noqa: E501
         name='dashboard_create_new_recipe'),
]
