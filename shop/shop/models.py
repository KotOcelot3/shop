from django.db import models


class Shop(models.Model):
    address = models.CharField(max_length=50, verbose_name="Адрес")

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

    def __str__(self):
        return f'{self.address}'


class City(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return f'{self.title}'
