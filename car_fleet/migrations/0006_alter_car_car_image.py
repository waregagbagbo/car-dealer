# Generated by Django 4.1.2 on 2022-10-25 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_fleet', '0005_rename_extras_extra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_image',
            field=models.ImageField(default='loom.jpg', upload_to='motors'),
        ),
    ]
