# Generated by Django 4.2.3 on 2023-07-17 16:04

import django.core.validators
from django.db import migrations, models
import pokemon_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_app', '0002_pokemon_captured_pokemon_date_captured_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(default='Unkown', validators=[django.core.validators.MinLengthValidator(25), django.core.validators.MaxLengthValidator(150)]),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='level',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='name',
            field=models.CharField(max_length=255, unique=True, validators=[pokemon_app.validators.validate_name]),
        ),
    ]
