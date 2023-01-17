from django.conf import settings
from django.db import models
from django.urls import reverse

from shared.django import TimeStampMixin


class Ticket(TimeStampMixin):
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="customer_tickets",
    )
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        default=None,
        on_delete=models.DO_NOTHING,
        related_name="manager_tickets",
    )

    header = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField(max_length=100, unique=True, default=None)

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return reverse("header_detail", kwargs={"slug": self.slug})
