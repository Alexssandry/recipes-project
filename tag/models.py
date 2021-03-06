import string
from random import SystemRandom

# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.text import slugify

# Create your models here.


# class Tag(models.Model):
#     name = models.CharField(max_length=200)
#     slug = models.SlugField(unique=True)

#     # Aqui começam os campos para a relação genérica
#     # Representa o model que queremos encaixar aqui
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

#     # Representa o id da linha do model descrito acima
#     # object_id = models.PositiveIntegerField()
#     object_id = models.CharField(max_length=200)
#     # Um campo que representa a relação genérica que conhece os
#     # campos acima (content_type, object_id)
#     content_object = GenericForeignKey('content_type', 'object_id')

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             rand_letters = ''.join(SystemRandom().choices(
#                 string.ascii_letters + string.digits,
#                 k=5,
#             ))
#             nova_slug = '{0}-{1}'.format(self.name, rand_letters)
#             self.slug = slugify(nova_slug)
#         return super().save(*args, **kwargs)

#     def __str__(self):
#         return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            rand_letters = ''.join(SystemRandom().choices(
                string.ascii_letters + string.digits,
                k=5,
            ))
            nova_slug = '{0}-{1}'.format(self.name, rand_letters)
            self.slug = slugify(nova_slug)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
