from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Category')
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='Tag')
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    view = models.PositiveIntegerField(verbose_name='View', default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100, verbose_name='Author', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag)
    on_top = models.BooleanField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Rating(models.Model):
    class RatingStarsChoices(models.TextChoices):
        STAR_5 = '5',
        STAR_4 = '4',
        STAR_3 = '3',
        STAR_2 = '2',
        STAR_1 = '1',
        STAR_0 = '0'

    value = models.CharField(max_length=1, choices=RatingStarsChoices.choices, default=RatingStarsChoices.STAR_0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
