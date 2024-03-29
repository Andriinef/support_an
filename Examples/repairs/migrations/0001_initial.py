# Generated by Django 4.1.4 on 2022-12-23 13:08

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
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
                    "mark",
                    models.CharField(max_length=50, verbose_name="марка автомобіля"),
                ),
                (
                    "model",
                    models.CharField(max_length=50, verbose_name="модель автомобіля"),
                ),
                (
                    "VIN_code",
                    models.CharField(max_length=50, verbose_name="VIN код автомобіля"),
                ),
                (
                    "number",
                    models.CharField(max_length=50, null=True, verbose_name="номер автомобіля"),
                ),
            ],
            options={
                "verbose_name": "Автомобіль",
                "verbose_name_plural": "Автомобілі",
            },
        ),
        migrations.CreateModel(
            name="Parts",
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
                ("name", models.CharField(max_length=50, verbose_name="Запчастина")),
                (
                    "quanti",
                    models.PositiveSmallIntegerField(default=1, verbose_name="Кількість одиницю"),
                ),
                (
                    "price",
                    models.FloatField(default=0.0, verbose_name="Ціна за одиницю"),
                ),
                ("total", models.FloatField(default=0.0, verbose_name="Загальна ціна")),
            ],
            options={
                "verbose_name": "Запчастина",
                "verbose_name_plural": "Запчастини",
            },
        ),
        migrations.CreateModel(
            name="PlacesToWork",
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
                ("name", models.CharField(max_length=50, verbose_name="Місце ремонта")),
            ],
            options={
                "verbose_name": "Місце ремонта",
                "verbose_name_plural": "Місця ремонта",
            },
        ),
        migrations.CreateModel(
            name="Works",
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
                ("name", models.CharField(max_length=50, verbose_name="Робота")),
                (
                    "hour",
                    models.FloatField(default=1, help_text="годин", verbose_name="Годин в роботі"),
                ),
                (
                    "price",
                    models.FloatField(
                        default=0.0,
                        help_text="грн.",
                        null=True,
                        verbose_name="Вартість роботи",
                    ),
                ),
                (
                    "guarantee",
                    models.PositiveSmallIntegerField(
                        default=1,
                        help_text="місяч",
                        null=True,
                        verbose_name="Гарантія на роботу",
                    ),
                ),
            ],
            options={
                "verbose_name": "Робота",
                "verbose_name_plural": "Роботи",
            },
        ),
        migrations.CreateModel(
            name="TypeRepair",
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
                ("name", models.CharField(max_length=150, verbose_name="Тип послуги")),
                (
                    "hour",
                    models.FloatField(default=1, help_text="годин", verbose_name="Годин для послуги"),
                ),
                (
                    "price",
                    models.FloatField(
                        default=0.0,
                        help_text="грн.",
                        null=True,
                        verbose_name="Вартість послуги",
                    ),
                ),
                (
                    "guarantee",
                    models.PositiveSmallIntegerField(
                        default=1,
                        help_text="місяч",
                        null=True,
                        verbose_name="Гарантія на послугу",
                    ),
                ),
                (
                    "type_works",
                    models.ManyToManyField(
                        related_name="work_repairs",
                        to="repairs.works",
                        verbose_name="Роботи",
                    ),
                ),
            ],
            options={
                "verbose_name": "Тип послуги",
                "verbose_name_plural": "Типи послуг",
            },
        ),
        migrations.CreateModel(
            name="Repair",
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
                    "description",
                    models.TextField(verbose_name="Опис послуги чи поломки"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("CREATED", "Нове замовленя від клієнта"),
                            ("CONFIRMED", "Підтверджено майстром"),
                            ("READY_TO_WORK", "Готова до роботи"),
                            ("PROGRESS", "В роботі"),
                            ("VERIFICATION", "Ремонт виконан"),
                            ("TESTS", "На тестуванні"),
                            ("RE_REPAIR", "На дороботці"),
                        ],
                        default="CREATED",
                        max_length=20,
                    ),
                ),
                (
                    "time_to_work",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        null=True,
                        verbose_name="Дата та час прийняття замовлення",
                    ),
                ),
                (
                    "time_to_ordering",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        null=True,
                        verbose_name="Дата та час оформлення замовлення",
                    ),
                ),
                (
                    "total_price",
                    models.IntegerField(default=0.0, verbose_name="Загальна вартість робот та послуг"),
                ),
                (
                    "car",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="car_repairs",
                        to="repairs.car",
                        verbose_name="Автомобіль",
                    ),
                ),
                (
                    "parts",
                    models.ManyToManyField(
                        related_name="part_repairs",
                        to="repairs.parts",
                        verbose_name="Запчастини",
                    ),
                ),
                (
                    "places_to_work",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="place_repairs",
                        to="repairs.placestowork",
                        verbose_name="Місце для ремонта",
                    ),
                ),
                (
                    "type_repair",
                    models.ManyToManyField(
                        related_name="type_repairs",
                        to="repairs.typerepair",
                        verbose_name="Тип послуги",
                    ),
                ),
            ],
            options={
                "verbose_name": "Замовлення",
                "verbose_name_plural": "Замовлення",
            },
        ),
    ]
