# Generated by Django 4.1.2 on 2022-12-13 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_fleet', '0005_rename_dealer_name_contact_dealer'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='avatar',
            field=models.ImageField(null=True, upload_to='media/profiles'),
        ),
    ]
