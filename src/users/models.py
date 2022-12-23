from django.db import models
from django.urls import reverse
from django.utils import timezone

from repairs.models.car import Car


class Address(models.Model):
    street = models.CharField("вулиця", max_length=100, default="----")
    number = models.PositiveSmallIntegerField("номер будинку", default="0")
    postal = models.IntegerField("поштова адреса", default="0000", blank=True)
    city = models.CharField("місто", max_length=100, default="----", blank=True)
    country = models.CharField("країна", max_length=100, default="----", blank=True)

    class Meta:
        verbose_name = "Домашня адреса"
        verbose_name_plural = "Домашня адреса"

    def __str__(self):
        return f"{self.street} - {self.number}"


class User(models.Model):
    first_name = models.CharField("Ім'я", max_length=50)
    last_name = models.CharField("Прізвеще", max_length=50)
    login_name = models.CharField("Логін", max_length=50, unique=True, db_index=True)
    User_email = models.EmailField(
        "Електронна пошта",
        max_length=70,
        blank=True,
        unique=True,
        help_text="Наприклад: user@gmail.com",
    )
    password = models.CharField(
        "Пароль", max_length=50, error_messages={"required": "Вкажить пароль"}
    )
    password_again = models.CharField(
        "Введіть пароль ще раз",
        max_length=50,
        error_messages={"required": "Вкажить пароль еще раз"},
    )
    phone = models.CharField("Номер телефона", max_length=50)
    phone_2 = models.CharField("Номер телефона 2", max_length=50, blank=True)
    car = models.ForeignKey(
        Car,
        blank=True,
        related_name="cars",
        verbose_name="Автомобіль",
        on_delete=models.CASCADE,
    )
    home_address = models.ForeignKey(
        Address,
        related_name="addresses",
        verbose_name="Домашня адреса",
        on_delete=models.CASCADE,
    )
    date_created = models.DateTimeField(
        default=timezone.now, verbose_name="Час публікації"
    )
    activated = models.BooleanField("Активувація", default=True)

    class Meta:
        verbose_name = "Кліент"
        verbose_name_plural = "Клиенти"

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name} {self.login_name}, тел.: {self.phone}"
        )

    def get_absolute_url(self):
        return reverse("login_name", kwargs={"pk": self.pk})
