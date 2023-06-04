from django.db import models
from user.models import User


class Product(models.Model):
    title = models.CharField(max_length=30, verbose_name="Товар")
    description = models.CharField(max_length=260, verbose_name="Описание")
    image = models.ImageField(upload_to="image/product/", null=False, blank=False,
                              verbose_name="Картинка")
    price = models.IntegerField(default=1000, verbose_name="Цена")
    sale = models.BooleanField(default=False, null=False, blank=False, verbose_name="Скидка")
    comment = models.ManyToManyField('Comment', verbose_name="Комментарий", null=True,
                                     related_name='products')
    discount = models.IntegerField(default=0, blank=True, null=True,
                                   verbose_name='Скидка в процентах')
    price_discount = models.IntegerField(default=0,  blank=True, null=True,
                                         verbose_name="Цена с скидкой")
    category = models.ManyToManyField('Category', verbose_name="Категория", related_name='products')

    # DISCOUNT = (
    #     (0, 'нет скидки'),
    #     (5, '5%'),
    #     (10, '10%'),
    #     (15, '15%'),
    #     (20, '20%'),
    #     (25, '25%'),
    #     (30, '30%'),
    # )
    # discount = models.IntegerField(default=0, blank=True, choices=DISCOUNT,
    #                                verbose_name='Скидка в процентах')

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return f'{self.title}'


class Category(models.Model):
    title = models.CharField(max_length=30, verbose_name="Название")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    title = models.CharField(max_length=30, verbose_name="Название")
    description = models.CharField(max_length=260, verbose_name="Текст комментария")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

    RATING = (
        (ONE, 1),
        (TWO, 2),
        (THREE, 3),
        (FOUR, 4),
        (FIVE, 5)
    )

    rating = models.IntegerField(default=0, choices=RATING, verbose_name='оценка')

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f'{self.title}'
