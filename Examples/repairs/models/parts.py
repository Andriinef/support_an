from django.db import models


class Parts(models.Model):

    name = models.CharField("Запчастина", max_length=50)
    quanti = models.PositiveSmallIntegerField("Кількість одиницю", default=1)
    price = models.FloatField("Ціна за одиницю", default=0.00, help_text="грн.")
    total_price = models.FloatField("Загальна ціна", default=0.00, help_text="грн.")

    class Meta:
        verbose_name = "Запчастина"
        verbose_name_plural = "Запчастини"

    def __str__(self):
        return f"{self.name}, ціна за одиницю: {self.price}, загальна ціна: {self.total_price}"
