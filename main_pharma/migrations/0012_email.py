# Generated by Django 3.1.7 on 2021-04-09 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_pharma', '0011_auto_20210409_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
    ]
