from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=30, verbose_name="Товар")
    description = models.CharField(max_length=260, verbose_name="Описание")
    image = models.ImageField(upload_to="image/product/", null=False, blank=False, verbose_name="Картинка")
    price = models.IntegerField(default=1000, verbose_name="Цена")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=30, verbose_name="Товар")
    product = models.ManyToManyField(Product, related_name='products', verbose_name='Товар')

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title
