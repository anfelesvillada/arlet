# Generated by Django 4.1.2 on 2022-10-24 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('latearrival', '0002_alter_latearrival_date_arrival_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latearrival',
            name='date_arrival',
            field=models.DateField(),
        ),
    ]