from django.contrib import admin
from django.contrib.admin import ModelAdmin

from tickets.models import Ticket


@admin.register(Ticket)
class TicketsAdmin(ModelAdmin):
    list_display = ("id", "customer", "manager", "header", "slug", "body")
    prepopulated_fields = {"slug": ("header",)}
