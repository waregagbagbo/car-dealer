# Generated by Django 4.1 on 2022-10-27 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_fleet', '0007_alter_car_car_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('used_car', 'Used_Car'), ('new_car', 'New_Car')], max_length=30)),
            ],
        ),
    ]
