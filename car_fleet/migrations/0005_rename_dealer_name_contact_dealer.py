# Generated by Django 4.1.2 on 2022-12-13 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_fleet', '0004_alter_contact_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='dealer_name',
            new_name='dealer',
        ),
    ]
