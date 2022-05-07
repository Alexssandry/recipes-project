from django.contrib import admin

from . import models

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Category, CategoryAdmin)


class RecipeAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Recipe, RecipeAdmin)
