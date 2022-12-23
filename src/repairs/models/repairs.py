from django.db import models
from django.urls import reverse
from django.utils import timezone


class Status(models.TextChoices):
    """Статуси для замовлень"""

    CREATED = "CREATED", "Нове замовленя від клієнта"
    CONFIRMED = "CONFIRMED", "Підтверджено майстром"
    READY_TO_WORK = "READY_TO_WORK", "Готова до роботи"
    PROGRESS = "PROGRESS", "В роботі"
    VERIFICATION = "VERIFICATION", "Ремонт виконан"
    TESTS = "TESTS", "На тестуванні"
    RE_REPAIR = "RE_REPAIR", "На дороботці"


class Repair(models.Model):
    """Замовлення на послуги"""

    car = models.ForeignKey(
        "repairs.Car",
        related_name="car_repairs",
        on_delete=models.CASCADE,
        verbose_name="Автомобіль",
        blank=True,
    )
    description = models.TextField(verbose_name="Опис послуги чи поломки")
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.CREATED,
    )
    time_to_work = models.DateTimeField(
        "Дата та час прийняття замовлення", null=True, blank=True, default=timezone.now
    )
    time_to_ordering = models.DateTimeField(
        "Дата та час оформлення замовлення", null=True, blank=True, default=timezone.now
    )
    places_to_work = models.ForeignKey(
        "repairs.PlacesToWork",
        related_name="place_repairs",
        on_delete=models.PROTECT,
        verbose_name="Місце для ремонта",
        null=True,
        blank=True,
    )
    type_repair = models.ManyToManyField(
        to="repairs.TypeRepair", verbose_name="Тип послуги", related_name="type_repairs"
    )
    parts = models.ManyToManyField(
        to="repairs.Parts", verbose_name="Запчастини", related_name="part_repairs"
    )
    total_price = models.IntegerField(
        "Загальна вартість робот та послуг", default=0.0, help_text="грн."
    )

    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"

    def __str__(self):
        return f"Заявка {self.id}, статус - {self.status}, авто - {self.car}, загальна вартість робот та послуг: {self.total_price} грн."

    def get_absolute_url(self):
        return reverse("repairs:detail", kwargs={"pk": self.pk})
