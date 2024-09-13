from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=111, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='продукты'
    )
    name = models.CharField(max_length=111, verbose_name='название')
    price = models.PositiveSmallIntegerField(verbose_name='цена')
    sales_percent = models.PositiveSmallIntegerField(
        verbose_name='скидки',
        null=True,
        blank=True,
        validators=[MaxValueValidator(100)]
    )
    description = models.TextField(verbose_name='описмание')
    short_descriptions = models.TextField(null=True)
    preview_image = models.ImageField()
    is_new = models.BooleanField()

    new_expiry_date = models.DateField()

    def __str__(self):
        return self.name

    # class Meta(models.Model):
    #     verbose_name_plural = 'Товары'
    #     verbose_name = 'Товар'


class ProductGallery(models.Model):
    gallery = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField()


# class ProductRating(models.Model):
#     """
#
#     """
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     rating = models.PositiveSmallIntegerField()

