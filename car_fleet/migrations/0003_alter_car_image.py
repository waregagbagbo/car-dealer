# Generated by Django 4.1.2 on 2022-10-25 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_fleet', '0002_rename_cars_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(upload_to='motors/% Y/% m/% d/'),
        ),
    ]
