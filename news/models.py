from django.db import models


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
    text = models.TextField(verbose_name='comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Rating(models.Model):
    view = models.IntegerField(verbose_name='Rating')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
