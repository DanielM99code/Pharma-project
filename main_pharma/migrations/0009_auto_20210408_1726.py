# Generated by Django 3.1.7 on 2021-04-08 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_pharma', '0008_aboutus_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='home',
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
