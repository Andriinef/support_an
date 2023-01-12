from django.contrib import admin

from tickets.models import Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = ("__add__",)


admin.site.register(Ticket)
