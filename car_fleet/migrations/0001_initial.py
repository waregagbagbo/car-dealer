# Generated by Django 4.1.2 on 2022-10-25 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cars/% Y/% m/% d/')),
                ('car_type', models.CharField(max_length=255)),
                ('make', models.CharField(max_length=255)),
                ('model_type', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('fuel', models.CharField(max_length=255)),
                ('engine_mode_size', models.CharField(max_length=255)),
                ('power', models.CharField(max_length=255)),
                ('gearbox', models.CharField(max_length=255)),
                ('number_of_seats', models.IntegerField()),
                ('doors', models.IntegerField()),
                ('color', models.CharField(max_length=255)),
                ('custom_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealer_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_1', models.CharField(max_length=255)),
                ('desc_2', models.CharField(max_length=255)),
                ('desc_3', models.CharField(max_length=255)),
                ('desc_4', models.CharField(max_length=255)),
                ('desc_5', models.CharField(max_length=255)),
                ('car', models.ManyToManyField(to='car_fleet.cars')),
            ],
        ),
        migrations.CreateModel(
            name='Extras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_1', models.CharField(max_length=30)),
                ('extra_2', models.CharField(max_length=30)),
                ('extra_3', models.CharField(max_length=30)),
                ('extra_4', models.CharField(max_length=30)),
                ('car', models.ManyToManyField(to='car_fleet.cars')),
            ],
        ),
    ]
