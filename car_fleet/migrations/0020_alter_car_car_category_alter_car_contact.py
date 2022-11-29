# Generated by Django 4.1.2 on 2022-11-29 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_fleet', '0019_alter_category_options_car_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_fleet.category'),
        ),
        migrations.AlterField(
            model_name='car',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_fleet.contact'),
        ),
    ]
