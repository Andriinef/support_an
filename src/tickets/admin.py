from django.contrib import admin

from tickets.models import Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = ("customer", "manager", "header", "slug", "body")
    prepopulated_fields = {"slug": ("header",)}


admin.site.register(Ticket, TicketAdmin)
