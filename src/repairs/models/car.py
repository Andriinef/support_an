from django.db import models


class Car(models.Model):
    mark = models.CharField("марка автомобіля", max_length=50)
    model = models.CharField("модель автомобіля", max_length=50)
    VIN_code = models.CharField("VIN код автомобіля", max_length=50)
    number = models.CharField("номер автомобіля", max_length=50, null=True)

    class Meta:
        verbose_name = "Автомобіль"
        verbose_name_plural = "Автомобілі"

    def __str__(self):
        return f"марка - {self.mark}, модель - {self.model}"
