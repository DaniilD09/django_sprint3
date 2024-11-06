from django.contrib import admin

from .import models


@admin.register(models.Post)
@admin.register(models.Category)
@admin.register(models.Location)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'text', 'pub_date',)


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description',)


class LocationAdmin(admin.ModelAdmin):
    search_fields = ('name',)


admin.site.empty_value_display = 'Не задано'
