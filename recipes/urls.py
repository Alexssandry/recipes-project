from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_home),
    path('recipes/<int:id>/', views.view_recipe),
]
