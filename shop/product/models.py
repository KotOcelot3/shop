from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=30, verbose_name="Товар")
    description = models.CharField(max_length=260, verbose_name="Описание")
    image = models.ImageField(upload_to="image/product/", null=False, blank=False, verbose_name="Картинка")
    price = models.IntegerField(default=1000, verbose_name="Цена")
    sale = models.BooleanField(default=False, null=False, blank=False, verbose_name="Скидка")

    DISCOUNT = (
        (0, 'нет скидки'),
        (5, '5%'),
        (10, '10%'),
        (15, '15%'),
        (20, '20%'),
        (25, '25%'),
        (30, '30%'),
    )
    discount = models.IntegerField(default=0, blank=True, choices=DISCOUNT, verbose_name='Скидка в процентах')
    # discount = models.IntegerField(default=0, blank=True, null=True, verbose_name='Скидка в процентах')

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return f'{self.title}'


class Category(models.Model):
    title = models.CharField(max_length=30, verbose_name="Название")
    product = models.ManyToManyField(Product, related_name='category', verbose_name='Товар')

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f'{self.title}'
