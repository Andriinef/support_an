from django.contrib import admin
from users.models import Address, User

admin.site.register(Address)
# admin.site.register(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "login_name": (
            "first_name",
            "last_name",
        )
    }
