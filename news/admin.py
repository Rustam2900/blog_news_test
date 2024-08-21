from django.contrib import admin
from .models import Category, Tag, Post, Comment, Rating

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Rating)

# @admin.register(Category)
# class ProductAdmin(TranslationAdmin):
#     list_display = ('slug', 'name')
#     list_filter = ('slug',)
