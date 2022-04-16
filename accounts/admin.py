# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # to control which fields are listed in the admin
    list_display = [
        "email",
        "username",
        # "age",
        "is_staff",
    ]
    # to actually edit the new custom fields like: age

    # used when editing a user
    fieldsets = UserAdmin.fieldsets  # + ((None, {"fields": ("age",)}),)
    # used when creating a user
    add_fieldsets = UserAdmin.add_fieldsets  # + ((None, {"fields": ("age",)}),)


admin.site.register(CustomUser, CustomUserAdmin)
