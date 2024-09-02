from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


# class User(models.Model):
#     """пользователь"""
#     first_name = models.CharField(max_length=111)
#
#     last_name = models.CharField(max_length=111)
#
#     email = models.EmailField(unique=True)
#     password = models.TextField()
#
#     phone_number = models.CharField(
#         max_length=22,
#         null=True,
#         blank=True
#     )
#     address = models.TextField()
#     avatar = models.ImageField()
#     birthdate = models.DateField()
#
#     date_join = models.DateTimeField(auto_now_add=True)
#     is_superuser = models.BooleanField()
#     is_staff = models.BooleanField()
#
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'
#         unique_together = ('first_name', 'last_name',)

class CustomUser(AbstractUser):


    email = models.EmailField(unique=True)
    avatar = models.ImageField()
    birthdate = models.DateField()
    phone_number = models.CharField(
            max_length=22,
            null=True,
            blank=True
        )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        unique_together = ('first_name', 'last_name',)




