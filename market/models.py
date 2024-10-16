from django.core.validators import MaxValueValidator, MinValueValidator
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

    def get_price_with_sales(self):
        """Возвращает цену с учётом скидки"""
        if self.price or self.sales_percent is None:
            return self.price  # Можешь вернуть 0 или другое значение, если одно из полей пустое

        if self.sales_percent == 0:
            return self.price

        return int((self.price / 100) * (100 - self.sales_percent))

    # class Meta(models.Model):
    #     verbose_name_plural = 'Товары'
    #     verbose_name = 'Товар'


class ProductGallery(models.Model):
    gallery = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField()

class ProductUserRating(models.Model):
    """Модель для рейтингов которые поставил пользователь для товара"""
    from users.models import CustomUser

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    name = models.CharField(max_length=111)
    email = models.EmailField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'product',)  # constraint - ограничение для бд

# class ProductRating(models.Model):
#     """
#
#     """
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     rating = models.PositiveSmallIntegerField()



class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    last_updated = models.DateTimeField()





