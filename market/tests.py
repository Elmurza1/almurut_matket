from django.test import TestCase
from django.utils.datetime_safe import datetime
from .models import Category, Product


class ProductListTestCase(TestCase):
    def test_product_list_success(self):
        response = self.client.get('/product-list/')
        self.assertEqual(response.status_code, 200)



class ProductDetailTestCase(TestCase):
    def test_product_detail_success(self):
        some_date = datetime(year=2024, month=3, day=4)
        category = Category.objects.create(name='phone')

        product = Product.objects.create(
            category=category,
            name='asus',
            price=50000,
            sales_procent=None,
            description='goood',
            new_expiry_date=some_date,
            preview_image='media/tovat/file-jpeg',
            is_new=True
        )

        response = self.client.get(f'/product-list/{product.id}/')

        self.assertEqual(response.status_code, 200)






