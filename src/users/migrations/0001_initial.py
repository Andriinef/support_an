# Generated by Django 4.1.4 on 2022-12-23 13:08

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("repairs", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "street",
                    models.CharField(
                        default="----", max_length=100, verbose_name="вулиця"
                    ),
                ),
                (
                    "number",
                    models.PositiveSmallIntegerField(
                        default="0", verbose_name="номер будинку"
                    ),
                ),
                (
                    "postal",
                    models.IntegerField(default="0000", verbose_name="поштова адреса"),
                ),
                (
                    "city",
                    models.CharField(
                        default="----", max_length=100, verbose_name="місто"
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        default="----", max_length=100, verbose_name="країна"
                    ),
                ),
            ],
            options={
                "verbose_name": "Домашня адреса",
                "verbose_name_plural": "Домашня адреса",
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50, verbose_name="Ім'я")),
                ("last_name", models.CharField(max_length=50, verbose_name="Прізвеще")),
                (
                    "login_name",
                    models.CharField(
                        db_index=True, max_length=50, unique=True, verbose_name="Логін"
                    ),
                ),
                (
                    "User_email",
                    models.EmailField(
                        blank=True,
                        help_text="Наприклад: user@gmail.com",
                        max_length=70,
                        unique=True,
                        verbose_name="Електронна пошта",
                    ),
                ),
                (
                    "password",
                    models.CharField(
                        error_messages={"required": "Вкажить пароль"},
                        max_length=50,
                        verbose_name="Пароль",
                    ),
                ),
                (
                    "password_again",
                    models.CharField(
                        error_messages={"required": "Вкажить пароль еще раз"},
                        max_length=50,
                        verbose_name="Введіть пароль ще раз",
                    ),
                ),
                (
                    "phone",
                    models.CharField(max_length=50, verbose_name="Номер телефона"),
                ),
                (
                    "phone_2",
                    models.CharField(
                        blank=True, max_length=50, verbose_name="Номер телефона 2"
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Час публікації"
                    ),
                ),
                (
                    "activated",
                    models.BooleanField(default=True, verbose_name="Активувація"),
                ),
                (
                    "car",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cars",
                        to="repairs.car",
                        verbose_name="Автомобіль",
                    ),
                ),
                (
                    "home_address",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="addresses",
                        to="users.address",
                        verbose_name="Домашня адреса",
                    ),
                ),
            ],
            options={
                "verbose_name": "Кліент",
                "verbose_name_plural": "Клиенти",
            },
        ),
    ]
