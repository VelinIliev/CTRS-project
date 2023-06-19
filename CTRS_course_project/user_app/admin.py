from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from CTRS_course_project.user_app.forms import UserEditForm, UserCreateForm

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    form = UserEditForm
    add_form = UserCreateForm
    fieldsets = (
        ("User info", {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email", "age")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions",), },),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
