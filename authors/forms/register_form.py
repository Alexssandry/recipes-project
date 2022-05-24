# from django.forms import Form, ModelForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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
#         exclude = ['first_name']


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['last_name'].widget.attrs['placeholder'] = 'Ex.: Pereira'
        self.fields['email'].widget.attrs['placeholder'] = \
            'Ex.: alexssandry.pereira@teste.django.com'

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat your password here',
        }),
        label='Password repeat',
        error_messages={
            'required': 'Required',
            'invalid': 'Field invalid',
        },
        help_text=('Repeat your password here.')
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

        labels = {
            'username': 'Username',
            'first_name': 'Firstname',
            'last_name': 'Lastname',
            'email': 'E-mail',
            'password': 'Password',
        }

        help_texts = {
            'email': 'The e-mail must be valid.'
        }

        error_messages = {
            'username': {
                'required': 'This field must not be empty.',
                'invalid': 'This field is invalid.'
            }
        }

        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder':
                'Type your username here. Ex.: alexssandry.pereira'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Type your password here',
            }),
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Ex.: Alexssandry',
            }),

        }

    def clean_password(self):
        data = self.cleaned_data.get('password')

        if 'atenção' in data or 'atencao' in data:
            raise ValidationError(
                'Não digite "atenção" no campo password.',
                code='invalid'
            )

        return data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        print('EMAIL: {0}'.format(email))
        exist = User.objects.filter(email=email).exists()
        if exist:
            raise ValidationError(
                'Email já foi utilizado',
                code='invalid'
            )

        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        print('USERNAME: {0}'.format(username))
        exist = User.objects.filter(username=username).exists()
        if exist:
            raise ValidationError(
                'username já foi utilizado!',
                code='invalid'
            )

        return username

    def clean(self):
        # cleaned_data = self.cleaned_data
        cleaned_data = super().clean()

        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise ValidationError({
                'password': 'Password and password2 most be equal.',
                'password2': 'Password and password2 most be equal.'
            })
