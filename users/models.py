from django.contrib.auth.models import AbstractUser
from django.db import models

from users.menegers import CustomUserManager



class CustomUser(AbstractUser):

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(
        unique=True,
        db_index=True
    )
    birth_date = models.DateField(null=True, blank=True)

    avatar = models.ImageField(upload_to='avatars/')
    phone_number = models.CharField(
                max_length=22,
                blank=True
            )

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

