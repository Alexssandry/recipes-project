from django.contrib import admin  # noqa

from . import models

# Register your models here.


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'slug',
    )
    list_display_links = (
        'id',
        'slug',
    )
    search_fields = (
        'id',
        'name',
        'slug',
    )

    list_editable = (
        'name',
    )
    ordering = (
        '-id',
    )
    prepopulated_fields = {
        'slug': ('name',)
    }
