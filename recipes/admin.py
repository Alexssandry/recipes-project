from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from tag.models import Tag

from . import models

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Category, CategoryAdmin)


class TagInlines(GenericStackedInline):
    model = Tag
    fields = 'name',
    extra = 1


@admin.register(models.Recipe)
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

    inlines = (TagInlines,)
