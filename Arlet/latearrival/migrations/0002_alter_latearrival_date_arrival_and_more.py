# Generated by Django 4.1.2 on 2022-10-24 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('latearrival', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latearrival',
            name='date_arrival',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='latearrival',
            name='observations',
            field=models.TextField(blank=True, default='NINGUNA', null=True),
        ),
    ]