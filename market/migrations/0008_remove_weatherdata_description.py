# Generated by Django 4.2 on 2024-10-14 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0007_weatherdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weatherdata',
            name='description',
        ),
    ]
