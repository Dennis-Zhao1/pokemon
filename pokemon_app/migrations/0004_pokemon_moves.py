# Generated by Django 4.2.3 on 2023-07-17 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('move_app', '0001_initial'),
        ('pokemon_app', '0003_alter_pokemon_description_alter_pokemon_level_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='moves',
            field=models.ManyToManyField(default=[1], to='move_app.move'),
        ),
    ]