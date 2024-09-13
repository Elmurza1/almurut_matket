# Generated by Django 4.2 on 2024-09-12 09:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_product_short_descriptions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sales_percent',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='скидки'),
        ),
    ]
