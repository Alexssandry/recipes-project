from django.urls import path

from . import views

# authors:register
app_name = 'authors'

urlpatterns = [
    path('authors/register/', views.view_register, name='register'),
]
