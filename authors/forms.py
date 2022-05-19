# from django.forms import Form, ModelForm
from django import forms
from django.contrib.auth.models import User

# METODO PADRAO DO DJANGO
#
# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = User
#         # fields = '__all__'
#         fields = [
#             'first_name',
#             'last_name',
#             'username',
#             'email',
#             'password',
#         ]


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]
