# Generated by Django 4.1.2 on 2022-10-24 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apprentice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LateArrival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_arrival', models.DateTimeField(auto_now_add=True)),
                ('observations', models.TextField(null=True)),
                ('document_apprentice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apprentice.apprentice')),
            ],
        ),
    ]
