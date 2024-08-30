from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Category, Tag, Post, Comment, Rating

admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Rating)


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['slug', ]
    search_fields = ['slug', ]


@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ['id', 'title', 'description', 'author', 'view', 'created_at', ]
    list_filter = ['author', 'category', 'on_top']
    search_fields = ['id', 'slug']
