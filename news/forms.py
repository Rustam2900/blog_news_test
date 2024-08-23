from django import forms
from .models import Post, Comment, Rating, Category, Tag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'slug']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'image', 'author', 'category', 'tags', 'on_top']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['value']
