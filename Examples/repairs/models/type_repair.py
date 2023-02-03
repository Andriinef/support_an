from django.db import models


class TypeRepair(models.Model):

    name = models.CharField(max_length=150, verbose_name="Тип послуги")
    hour = models.FloatField("Годин для послуги", default=1, help_text="годин")
    type_works = models.ManyToManyField(to="repairs.Works", verbose_name="Роботи", related_name="work_repairs")
    price = models.FloatField("Вартість послуги", null=True, default=0.00, help_text="грн.")
    guarantee = models.PositiveSmallIntegerField("Гарантія на послугу", null=True, default=1, help_text="місяч")

    class Meta:
        verbose_name = "Тип послуги"
        verbose_name_plural = "Типи послуг"

    def __str__(self):
        return f"{self.name} - вартість послуги: {self.price}"
