from django.db import models


class PlacesToWork(models.Model):

    name = models.CharField("Місце ремонта", max_length=50)

    class Meta:
        verbose_name = "Місце ремонта"
        verbose_name_plural = "Місця ремонта"

    def __str__(self):
        return self.name
