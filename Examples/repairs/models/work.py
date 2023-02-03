from django.db import models


class Works(models.Model):

    name = models.CharField(max_length=50, verbose_name="Робота")
    hour = models.FloatField("Годин в роботі", default=1, help_text="годин")
    price = models.FloatField("Вартість роботи", null=True, default=0.00, help_text="грн.")
    guarantee = models.PositiveSmallIntegerField("Гарантія на роботу", null=True, default=1, help_text="місяч")

    class Meta:
        verbose_name = "Робота"
        verbose_name_plural = "Роботи"

    def __str__(self):
        return f"{self.name} - вартість роботи: {self.price}"
