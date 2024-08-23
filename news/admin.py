from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Category, Tag, Post, Comment, Rating

# admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Rating)


@admin.register(Category)
class QuoteAdmin(ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['slug', ]
    search_fields = ['slug', ]
