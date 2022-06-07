from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# Users = get_user_model()
# Users2 = User()
User = get_user_model()

# print(Users.objects.all())
# print(Users2.objects.all())


class Profile(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='', blank=True)

    def __str__(self):
        return self.author.first_name
