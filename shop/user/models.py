from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=20, verbose_name='Никнейм', unique=True,)
    email = models.EmailField(null=False, blank=False, verbose_name='Почта')
    images = models.ImageField(upload_to="image/user/", null=False, blank=False, verbose_name="Картинка")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
