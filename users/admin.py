from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    search_fields = ("email", "first_name", 'last_name')
    list_display = ("email", "is_staff")
