# Generated by Django 4.2 on 2024-09-06 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_alter_product_sales_percent_productrating'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductRating',
        ),
    ]
