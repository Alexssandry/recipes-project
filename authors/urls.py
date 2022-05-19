from django.urls import path

from . import views

# authors:register
app_name = 'authors'

urlpatterns = [
    path('register/', views.view_register, name='register'),
    path('register/create/', views.view_register_create, name='register_create'),  # noqa: E501
]
