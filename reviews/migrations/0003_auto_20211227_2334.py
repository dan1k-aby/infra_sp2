# Generated by Django 2.2.16 on 2021-12-27 17:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20211014_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.SmallIntegerField(error_messages={'validators': 'Оценка может быть от 1 до 10'}, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Оценка'),
        ),
    ]
