from django.contrib.auth.models import AbstractUser
from django.db import models
from shop.models import Shop, City


class User(AbstractUser):
    email = models.EmailField(null=False, blank=False, verbose_name="Почта", unique=True)
    images = models.ImageField(upload_to="image/user/", null=False, blank=False, verbose_name="Картинка")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f'{self.username}'


class Vacancies(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название вакансии", unique=True)
    Responsibilities = models.CharField(max_length=200, verbose_name="Обязанности")
    Requirements = models.CharField(max_length=200, verbose_name="Требования")
    Conditions = models.CharField(max_length=200, verbose_name="Условности")
    price = models.IntegerField(default=0, verbose_name='Оплата', null=False, blank=False)
    shop = models.ManyToManyField(Shop, null=False, verbose_name="Адрес магазина")
    city = models.ManyToManyField(City, null=False, verbose_name="Город")
    
    
    class Meta:
        verbose_name = "Вакансии"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return f'{self.title}'

