# Generated by Django 3.1.7 on 2021-04-24 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_pharma', '0019_auto_20210424_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=200),
        ),
    ]
