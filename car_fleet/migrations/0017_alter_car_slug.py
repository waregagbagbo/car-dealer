# Generated by Django 4.1 on 2022-11-11 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_fleet', '0016_category_remove_car_car_type_car_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
