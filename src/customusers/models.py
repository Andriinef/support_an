from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from customusers.constants.roles import Role
from customusers.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField("Ім'я", max_length=50, blank=True)
    last_name = models.CharField("Прізвеще", max_length=50, blank=True)
    last_login = models.CharField("Логін", max_length=50, blank=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField("Персонал", default=False)
    is_active = models.BooleanField("Активний", default=True)

    role = models.CharField("Статус", max_length=7, choices=Role.values())

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        managed = True
        verbose_name = "Користувач"
        verbose_name_plural = "Користувачі"

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.email
