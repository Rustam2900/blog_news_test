from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from .models import Post, Category


@receiver(pre_save, sender=Post)
def post_pre_save(seder, instance, **kwargs):
    instance.field = instance.field.upper()


"""
salom
"""


@receiver(post_save, sender=Post)
def my_handler(sender, instance, created, **kwargs):
    if created:
        print(f"{instance} yaratildi")


@receiver(pre_delete, sender=Post)
def my_handler(sender, instance, **kwargs):
    print(f"{instance} o'chirilmoqda")


@receiver(post_delete, sender=Post)
def my_handler(sender, instance, **kwargs):
    print(f"{instance} o'chirildi")


@receiver(pre_delete, sender=Category)
def delete_related_objects(sender, instance, **kwargs):
    related_objects = Post.objects.filter(my_model=instance)
    related_objects.delete()
    print(f"{instance} bilan bog'liq obyektlar o'chirildi")
