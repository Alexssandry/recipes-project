from django.contrib import admin

from . import models

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Category, CategoryAdmin)


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'author',
        'created_at',
        'is_published',
    )
    list_display_links = (
        'title',
    )
    search_fields = (
        'id',
        'title',
        'description',
        'slug',
        'created_at',
    )
    list_filter = (
        'category',
        'author',
        'is_published',
    )
    list_per_page = 20
    list_editable = (
        'is_published',
    )
    ordering = (
        '-id',
    )
    prepopulated_fields = {
        'slug': ('title',)
    }


admin.site.register(models.Recipe, RecipeAdmin)
