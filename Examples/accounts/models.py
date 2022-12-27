from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(
        "Вік", null=True, blank=True, help_text="Вкажить свій вік."
    )

    class Meta:
        verbose_name = "Акаунт"
        verbose_name_plural = "Акаунти"
