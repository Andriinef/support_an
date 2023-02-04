from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = ["user_permissions", "groups"]
    readonly_fields = [
        # "last_login",
        "email",
        "password",
        "is_superuser",
        "is_staff",
        "is_active",
    ]
    list_display = [
        "id",
        "email",
        "first_name",
        "role",
        "is_superuser",
        "is_staff",
        "is_active",
    ]
    list_filter = [
        "role",
        "is_superuser",
        "is_staff",
        "is_active",
    ]
    search_fields = [
        "email",
        "first_name",
        "role",
        "is_superuser",
        "is_staff",
        "is_active",
    ]
