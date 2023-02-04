from django.contrib import admin
from django.contrib.admin import ModelAdmin

from comments.models import Comment


@admin.register(Comment)
class CommentsAdmin(ModelAdmin):
    list_display = ["body", "ticket", "user"]
