# Generated by Django 4.2 on 2024-08-23 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_category_name_alter_post_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
