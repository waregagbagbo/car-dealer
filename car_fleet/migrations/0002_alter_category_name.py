# Generated by Django 4.1.2 on 2022-11-29 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_fleet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('1', 'Used_Car'), ('2', 'New_Car')], default='used_car', max_length=255),
        ),
    ]
