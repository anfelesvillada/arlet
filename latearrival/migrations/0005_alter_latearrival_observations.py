# Generated by Django 4.1.2 on 2022-10-28 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('latearrival', '0004_alter_latearrival_observations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latearrival',
            name='observations',
            field=models.CharField(blank=True, default='NINGUNA', max_length=60, null=True),
        ),
    ]
